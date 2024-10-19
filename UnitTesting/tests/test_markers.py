# Marking test functions and selecting them for a run
# -- You can then restrict a test run to only run tests marked with mention functions
import sys

import pytest

from UnitTesting.my_app.mathematical_equation import add, sub, mult, div
from UnitTesting.my_app.myValidation import validation_age


def test_add_number():
    assert add(5,6) == 11

def test_subtract_number():
    assert sub(10,5) == 5

@pytest.mark.skip(reason="just wanna skip it for testing mark.skip")
def test_multiply_number():
    assert mult(10,5) == 50

@pytest.mark.skipif( sys.version_info > (3, 9), reason="testing skip with condition")
def test_divide_number():
    assert div(10,5) == 2

def test_invalid_divide_number():
    with pytest.raises(ValueError, match= "200 cannot be greater than 10"):
        assert div(10,200) == 1

def test_validate_over_age():
    # Get ValueError and Print it
    with pytest.raises(ValueError, match="Age cannot be greater than 50"):
        validation_age(60)

# XFail: mark test functions as expected to fail
@pytest.mark.xfail(reason="testing skip")
def test_add_list():
    assert add([1,2,3],[4,5,6]) == [1,2,3,4,5,6,7]
    raise Exception()
