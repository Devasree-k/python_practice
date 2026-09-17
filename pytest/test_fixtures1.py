# import pytest
#
# @pytest.fixture
# def login_data():
#     return {
#         "username": "admin",
#         "password": "Test@123"
#     }
# def test_valid_username(login_data):
#     assert login_data["username"] != ""
# def test_valid_password(login_data):
#     assert login_data["password"] != ""
# def test_correct_username(login_data):
#     assert login_data["username"] == "admin"


import pytest


@pytest.fixture
def login_data():
    print("Preparing login data")

    data = {
        "username": "deva",
        "password": "Test@123"
    }

    yield data

    print("Cleaning up login data")


def test_valid_username(login_data):
    assert login_data["username"] != ""


def test_valid_password(login_data):
    assert login_data["password"] != ""


def test_correct_username(login_data):
    assert login_data["username"] == "deva"