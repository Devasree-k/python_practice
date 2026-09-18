
# pytest is a highly popular, open-source Python testing framework designed to help developers
#  write everything from simple unit tests to complex functional and integration tests


def test_valid_login():
    username="deva"
    password="Test@123"

    assert username == "deva"
    assert password =="Test@123"
    print("Valid login")


def test_empty_username():
    username = ""
    password = "Test@123"

    login_valid = username != "" and password != ""
    assert login_valid == False

def test_password_mismatch():
    password = "Test@123"
    confirm_password = "Test@1234"

    passwords_match = password == confirm_password

    assert passwords_match == False


# function call is not required as we use pytest framework.
test_valid_login()
test_empty_username()
test_password_mismatch()
