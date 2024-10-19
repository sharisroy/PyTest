
# sharing fixtures across classes, modules, packages or session
# -- fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or projects.
# -- fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.

from datetime import datetime

import pytest

from UnitTesting.my_app.utiles import Student


@pytest.fixture(scope='package')
def dummy_student():
    print("Creating a dummy student...")
    return Student("Haris", datetime(2000, 1, 1), "Mirpur")


def test_student_get_age(dummy_student):
    age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == age

def test_student_add_credits(dummy_student):
    dummy_student.add_credits(100)
    assert dummy_student.get_credits() == 100

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 100

