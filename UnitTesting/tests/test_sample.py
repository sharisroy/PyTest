from UnitTesting.my_app.mathematical_equation import *


def test_add_number():
    assert add(1, 2) == 3

def test_add_string():
    assert add("Hello", "World") == "HelloWorld"

def test_divide_number():
    assert div(10,3) == 3

def test_bool_false():
    assert False, "Assertion False"


class TestSample:
    def test_add_number(self):
        assert add(1, 2) == 4, "failed test intentionally"
    def test_add_string(self):
        assert add("Hello", "World") == "HelloWorld"

