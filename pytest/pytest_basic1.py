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
    
    
