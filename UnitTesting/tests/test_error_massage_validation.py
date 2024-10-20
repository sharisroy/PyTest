
# Asserting Expected Exceptions
#  -- create some error and asserting the error





import pytest

from UnitTesting.my_app.myValidation import validation_age

def test_validate_valid_age():
    validation_age(10)

def test_validate_negative_age():
    # Get ValueError and Print it
    with pytest.raises(ValueError) as error_info:
        validation_age(-10)
    print(str(error_info.value))
    assert  str(error_info.value) == "Age cannot be negative"

def test_validate_over_age():
    # Get ValueError and Print it
    with pytest.raises(ValueError, match="Age cannot be greater than 50")as error_info:
        # print(str(error_info.value))
        validation_age(60)

