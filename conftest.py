import pytest
from datetime import datetime


@pytest.fixture(scope="session")
def currencies_with_rub(request):
    curs = {
        "USD": 91.001017178,
        "EUR": 110.004322,
        "UZS": 125
    }
    yield curs


@pytest.fixture(scope="function")
def currencies_for_check_file():
    rates = {
        "USD": 91.001017178,
        "EUR": 110.004322,
        "UZS": 125
    }
    yield rates


@pytest.fixture(scope="session", autouse=True)
def tests_timer():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"\nTest runtime: {execution_time} sec.")
