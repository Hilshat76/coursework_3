import pytest

from src.functions import mask_number


def test_mask_number():
    assert mask_number('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert mask_number('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert mask_number("Счет 35158586384610753655") == "Счет **3655"


def test_mask_number__IndexError():
    with pytest.raises(IndexError):
        mask_number('')
        mask_number(' ')


def test_mask_number__NameError():
    with pytest.raises(NameError):
        mask_number(Maestro - 1596837868705199)
        mask_number(Visa-Classic-6831982476737658)


def test_mask_number__TypeError():
    with pytest.raises(TypeError):
        mask_number()
