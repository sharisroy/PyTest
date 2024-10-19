
# sharing fixtures across classes, modules, packages or session
# -- fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or projects.
# -- fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.

from datetime import datetime


from UnitTesting.my_app.utiles import get_topper


def test_student_get_age(dummy_student):
    age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 100

def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("Haris", 20),
        make_dummy_student("Karim", 30),
        make_dummy_student("Mahir", 40),
        make_dummy_student("Bijoy", 39)
    ]
    topper = get_topper(students)
    assert topper == students[2]
