import pytest
import json
from src.loading_data import load_operations

@pytest.fixture
def operations_json():
    with open('../operations.json', 'rt', encoding='utf') as file:
        return json.load(file)

def test_load_operations():
    operations = load_operations('../operations.json')
    assert isinstance(operations, list)
    assert len(operations) <= 5
    for operation in operations:
        assert operation['state'] == "EXECUTED"
    assert operations == sorted(operations, key=lambda x: str(x.get('date')), reverse=True)

def test_load_operations_empty_file(tmp_path):
    operations_test_file = tmp_path / 'operations_test.json'
    with open(operations_test_file, 'w', encoding='utf') as file:
        json.dump([], file)
    operations = load_operations(operations_test_file)
    assert operations == []

def test_load_operations_no_executed_operations(operations_json, tmp_path):
    for operation in operations_json:
        operation['state'] = "CANCELED"
    operations_test_file = tmp_path / 'operations_test.json'
    with open(operations_test_file, 'w', encoding='utf') as file:
        json.dump(operations_json, file)
    operations = load_operations(operations_test_file)
    assert operations == []

def test_load_operations_more_than_five_executed_operations(operations_json, tmp_path):
    for i in range(10):
        operations_json.append({'state': "EXECUTED", 'date': f"2024-05-23{i}"})
    operations_test_file = tmp_path / 'operations_test.json'
    with open(operations_test_file, 'w', encoding='utf') as file:
        json.dump(operations_json, file)
    operations = load_operations(operations_test_file)
    assert len(operations) == 5
