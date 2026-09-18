

# Try to avoid hard coding so use input function

#'''
# import sys
# full_name = sys.argv[1]
# print("Full name ", full_name)
#'''


a= int(input("Enter number 1 "))
b= int(input("Enter number 2 "))
print(a+b)

def test_valid_login():
    username="deva"
    password="Test@123"

    assert username!=""
    assert password!=""
    print("test_valid_login passed!")


def test_invalid_login():
    username=""
    password="wrong"
    assert username==""
    print("test_invalid_login passed!")


test_valid_login()

test_invalid_login()
    
    


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

    print("empty username validation")

def test_password_mismatch():
    password = "Test@123"
    confirm_password = "Test@1234"

    passwords_match = password == confirm_password

    assert passwords_match == False
    print("password mismatch validation passed ")


test_valid_login()
test_empty_username()
test_password_mismatch()



#schedular can't give input at runtime we have to give that manually so for that we can import the sys and use the sys.argv[index]
# for that sys.argv to run it use the Run--Customize option and give the customise message to run .





