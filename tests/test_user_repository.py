from lib.user_repository import UserRepository

""" when i call the all function - all users are shown """

def test_users_are_seen(db_connection):
    repository = UserRepository(db_connection)
    assert repository.all() == [
        'User(Katie, Katie@hotmail.co.uk, katieuser, password123)'
    ]


    