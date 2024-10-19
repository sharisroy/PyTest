import pytest

from UnitTesting.my_app.mathematical_equation import add


def test_add_number():
    assert add(1, 2) == 3

def test_add_string():
    assert add("Hello", "World") == "HelloWorld"


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input_1, test_input_2, expected_result", [(1, 2, 3), ("HarisChandra", "Roy", "HarisChandraRoy"),([1,2], [3], [1, 2, 3])], ids=["num", "str", "list"])
def test_add(test_input_1, test_input_2, expected_result):
    assert add(test_input_1, test_input_2) == expected_result


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


# To get all combinations of multiple parametrized arguments you can stack parametrize decorators:
# This will run the test with the arguments set to x=0/y=2, x=1/y=2, x=0/y=3, and x=1/y=3 exhausting parameters in the order of the decorators.
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])

def test_add(x, y):
    assert add(x, y) == x + y