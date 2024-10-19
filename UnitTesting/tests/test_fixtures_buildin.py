
# The tmpdir_factory is a session-scoped fixture which can be used to create arbitrary temporary directories from any other fixture or test
# the capsys fixture is a built-in tool that allows you to capture and test output in your unit tests.

import json
import os

from UnitTesting.my_app.utiles import save_dict

def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, 'test.json')
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "Done\n"

