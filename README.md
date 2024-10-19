# PyTest

1. download and install required packages
        <br /> pip install -r requirements.txt <br />
2. run using terminal -<br />

        1. run full project - pytest directory_name(pytest Pytest_Topics)
        2. run single file - pytest directory_name/test_file_name(pytest Pytest_Topics/test_module_number.py)
        3. run single module - pytest directory_name/test_file_name::module_name (pytest Pytest_Topics/test_assertion.py::test_character_match)
        4. search and run module name - pytest -v -k module_name (pytest -v -k test_character_match)
        5. print function - pytest directory_name -s (pytest Pytest_Topics -s)
        6. show extra info on xfailed, xpassed, and skipped tests - pytest directory_name -rxXs( pytest test_markers.py -rxXs)


        NB: Go to the project directory and type the command

