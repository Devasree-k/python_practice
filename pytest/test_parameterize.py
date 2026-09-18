import pytest
#
# @pytest.mark.parametrize("username",[
#     "deva","anu","priya",""
# ])
#
# def test_username(username):
#     assert username is not None


# @pytest.mark.parametrize("username,password,email,expected",[
#     ("deva","Test@123","deva@gmail.com",True),
#     ("deva","wrong@123","deva.com",False),
#     ("","Test@123","",False)
# ])
#
# def test_login(username,password,email, expected):
#     login_valid = username!="" and password =="Test@123"
#     assert login_valid == expected

# def test_email(username,password,email, expected):
#     email_valid = "@" in email and "." in email
#     assert email_valid == expected



# with parameters and ID
# @pytest.mark.parametrize(
#     "age,expected",
#     [
#         (17, False),
#         (18, True),
#         (60, True),
#         (61, False),
#     ],
#     ids=[
#         "below_minimum",
#         "minimum",
#         "maximum",
#         "above_maximum"
#     ]
# )
# def test_age_validation(age, expected):
#     valid_age = 18 <= age <= 60
#     assert valid_age == expected



# without an id and all age_validation_cases

# @pytest.mark.parametrize(
#     "age,expected",
#     [
#         (17, False),
#         (18, True),
#         (19,True),
#         (30,True),
#         (60, True),
#         (61, False),
#     ]
# )
#
# def test_age_validation(age,expected):
#     valid_age = 18<=age<=60
#     assert valid_age == expected


@pytest.mark.parametrize("username,password,expected",[
    ("anu","1234567",False),
    ("priya","12345678",True),
    ("kayal","123456789",True),
    ("Pavi","12345678901234",True)
])

def test_password_length(username,password,expected):
    valid_password=password.__len__()>=8
    assert valid_password == expected


