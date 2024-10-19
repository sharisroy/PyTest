import json
from datetime import datetime


def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("Done")


class Student:
    def __init__(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = 0

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits




class Student2:
    def __init__(self, name, dob, branch, credit):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credit

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits

def get_topper(students):
    return max(students, key= lambda student: student.get_credits())
