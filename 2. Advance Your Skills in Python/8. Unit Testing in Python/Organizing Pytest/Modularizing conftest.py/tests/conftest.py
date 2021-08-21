# from utility.cities import city_list_location #pylint:disable=unused-import
# from utility.data_processing import process_data #pylint:disable=unused-import

"""
This file is for walkthrough purposes only.
Normally, conftest.py file should be located directly under the "tests/" folder.
"""


pytest_plugins = [
    "tests.utility.cities",
    "tests.utility.data_processing"
]
