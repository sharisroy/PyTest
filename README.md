# PyTest

1. download and install required packages - pip install -r requirements.txt
2. run using terminal -
        1. run full project - Go to project directory and type pytest directory_name(pytest Pytest_Topics)
        2. run single file - Go to project directory and type pytest directory_name/test_file_name(pytest Pytest_Topics/test_module_number.py)
        3. run single module - Go to project directory and type pytest directory_name/test_file_name::module_name
            (pytest Pytest_Topics/test_assertion.py::test_character_match)
        4. search and run module name - pytest -v -k module_name (pytest -v -k test_character_match)
        NB: if need more information use -v (pytest -v Pytest_Topics/test_module_number.py)
3.
