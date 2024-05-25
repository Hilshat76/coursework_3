import pytest

from src.functions import formatting_date


def test_formatting_date():
    assert formatting_date('2019-12-07T06:17:14.634890') == '07.12.2019'
    assert formatting_date('2018-12-23T11:47:52.403285') == '23.12.2018'


def test_formatting_date__ValueError():
    with pytest.raises(ValueError):
        formatting_date('20a9-12-07T06:17:14.634890')
        formatting_date('2019-13-07T06:17:14.634890')
        formatting_date('2019-12-35T06:17:14.634890')
        formatting_date('2019-12-07 06:17:14.634890')
        formatting_date('2019-12-07T25:17:14.634890')
        formatting_date('2019-12-07T06:73:14.634890')
        formatting_date('')
        formatting_date(' ')


def test_formatting_date__TypeError():
    with pytest.raises(TypeError):
        formatting_date()
