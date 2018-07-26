# -- FILE: features/steps/example_steps.py
import os
import glob
from pathlib import Path
from behave import given, when, then, step

from app import make_file


def test_f():
    print('test')
    print(glob.glob("static/downloads/*.sql"))


@given(u'I want SQL')
def step_impl(context):
    pass


@when(u'I generate test SQL with start day {start:d} and end day {end:d}')
def step_impl(context, start, end):  # -- NOTE: number is converted into integer
    start = int(start)
    end = int(end)
    make_file(start, end)
    assert start != None


@then(u'I get SQL')
def step_impl(context):
    my_file = Path("static/downloads/fakewarnings.sql")
    assert my_file.is_file() is True


@then(u'The SQL file should contain {SQL_Term}')
def step_impl(context, SQL_Term):
    file_path = "static/downloads/fakewarnings.sql"
    my_file = Path(file_path)
    assert my_file.is_file() is True
    print('first line is')
    with open(file_path, "r") as f:
        print('first line is')
        lines = f.readlines()
        print('first line is')
        print(lines[0])
        assert SQL_Term in lines[0]


@when(u"I generate SQL with start day {start} and end day {end}")
def step_impl(context, start, end):
    start = int(start)
    end = int(end)
    make_file(start, end)
    my_file = Path("static/downloads/fakewarnings.sql")
    test_f()
    print(my_file)
    assert start != None


@step(u"teardown")
def step_impl(context):
    file_path = "static/downloads/fakewarnings.sql"
    my_file = Path(file_path)
    assert my_file.is_file() is True
    try:
        os.remove(file_path)
    except OSError:
        pass
