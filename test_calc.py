import pytest
import calc


@pytest.mark.parametrize("value, currency, result", [
    (555, "USD", 50505.56453379),
    (100, "EUR", 11000.4322),
    (12500, "UZS", 100.0),
    (pytest.param(1, "BTC", 1000, marks=pytest.mark.xfail))])
def test_convert_to_rub(currencies_with_rub, value, currency, result):
    check = calc.to_rub(value, currency, currencies_with_rub)
    assert check == result


def test_compare_currencies(currencies_for_check_file: dict):
    calc.write_currencies_to_file(currencies_for_check_file)
    currencies_dictionary = {}
    with open("currencies.txt", "r") as curs_w:
        for string in curs_w:
            line = string.split(' ')
            currencies_dictionary[line[0]] = line[1]
    assert currencies_dictionary != currencies_for_check_file


def test_not_write_error():
    with pytest.raises(PermissionError):
        with open("read_only.txt", "w") as write_test:
            write_test.write("SeoSeoSeo")
