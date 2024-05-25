import pytest, json
from src.main import main


@pytest.fixture
def operations_json():
    return [
        {"date": "01.01.2024", "description": "Перевод со счета на счет", "to": "1234567890", "from": "0987654321",
         "operationAmount": {"amount": 25780.71, "currency": {"name": "USD"}}},
        {"date": "01.01.2024", "description": "Открытие вклада", "to": "1234567890", "from": None,
         "operationAmount": {"amount": 92688.46, "currency": {"name": "руб."}}},
    ]


@pytest.fixture
def mock_load_operations(operations_json, monkeypatch, tmp_path):
    operations_file = tmp_path / 'test_main_operations.json'
    with open(operations_file, "w") as f:
        json.dump(operations_json, f)

    def mock_load_operations(path):
        return operations_json

    monkeypatch.setattr("src.main.load_operations", mock_load_operations)
    return operations_file


def test_main(mock_load_operations, capsys, monkeypatch):
    def mock_formatting_date(date):
        return date

    def mock_mask_number(number):
        return "*" * len(number)

    monkeypatch.setattr("src.main.formatting_date", mock_formatting_date)
    monkeypatch.setattr("src.main.mask_number", mock_mask_number)

    main()

    captured = capsys.readouterr().out
    expected_output = """
01.01.2024 Перевод со счета на счет
********** -> **********
25780.71 USD

01.01.2024 Открытие вклада
**********
92688.46 руб.
"""
    assert captured == expected_output
