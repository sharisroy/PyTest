from unittest import mock
from unittest.mock import call

import pytest

from UnitTesting.mock_data.sample import guess_number, get_ip, random_sum, silly


def test_guess_number():
    assert guess_number(3) == "You Won!"

@mock.patch('UnitTesting.mock_data.sample.roll_dice')
def test_mock_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "You Won!"
    mock_roll_dice.assert_called_once_with()


@mock.patch('UnitTesting.mock_data.sample.random.randint')
def test_random_number(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls = [call(1, 10), call(1, 7)])


@pytest.mark.parametrize('number,expected', [(3, "You Won!"), (4, "You Lost!"), (3, "You Lost!")])
@mock.patch('UnitTesting.mock_data.sample.roll_dice')
def test_mock_number_parametrize(mock_roll_dice, number, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(number) == expected
    mock_roll_dice.assert_called_once_with()


def test_get_real_ip():
    print(get_ip())



@mock.patch('UnitTesting.mock_data.sample.requests.get')
def test_get_ip(mock_request_get):
    mock_request_get.return_value = mock.Mock(name='mock response', **{"status_code": 200,
                                                       "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_request_get.assert_called_once_with("https://httpbin.org/ip")


@mock.patch('UnitTesting.mock_data.sample.random.randint')
@mock.patch('UnitTesting.mock_data.sample.time.time')
@mock.patch('UnitTesting.mock_data.sample.requests.get')
def test_silly(mock_requests_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params["timestamp"]
    mock_randint.return_value = test_params["number"]
    mock_requests_get.return_value = mock.Mock(**{"status_code": 200,
                                                  "json.return_value":
                                                      {"args": test_params}})

    assert silly() == test_params




