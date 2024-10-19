import random
import time

import requests
from gevent.libev.corecext import timer

from UnitTesting.mock_data.dice import roll_dice


def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You Won!"
    else:
        return "You Lost!"



def random_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 7)
    return a + b

def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()["origin"]





def silly():
    params = {
        "timestamp": time.time(),
        "number": random.randint(1, 6)
    }
    response = requests.get("https://httpbin.org/ip", params)
    if response.status_code == 200:
        return response.json()["args"]

