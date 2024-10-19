
# We can define the fixture functions in this file to make them accessible across multiple test files.


from datetime import datetime
import pytest

from UnitTesting.my_app.utiles import Student2


@pytest.fixture
def dummy_student():
    print("Creating a dummy student...")
    return Student2("Haris", datetime(2000, 1, 1), "Mirpur", 100)

@pytest.fixture
def make_dummy_student(dummy_student):
    def _make_dummy_student(name, credit):
        return Student2(name, datetime(2000, 1, 1), "Mirpur", credit)
    return _make_dummy_student

