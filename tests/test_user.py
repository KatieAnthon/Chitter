from lib.user import User


""" test user inputs are initialised in the class"""
def test_user_variables_are_initialised():
    user = User('sophie', 'sophie@hotmail.co.uk', 'sophieuser', 'password!', True)
    assert user.name_of_user == 'sophie'
    assert user.email_address == 'sophie@hotmail.co.uk'
    assert user.username == 'sophieuser'
    assert user.user_password == 'password!'

""" when the same value is entered - the class recognises that it is not 2 separate items"""

def test_user_variables_do_not_duplicate():
    user = User('sophie', 'sophie@hotmail.co.uk', 'sophieuser', 'password!', True)
    user2 = User('sophie', 'sophie@hotmail.co.uk', 'sophieuser', 'password!', True)
    assert user == user2

""" when returning the user input - the digested information is readable"""

def test_user_formatting():
    user = User('sophie', 'sophie@hotmail.co.uk', 'sophieuser', 'password!', True)

    assert str(user) == 'User(sophie, sophie@hotmail.co.uk, sophieuser, password!, True)'

