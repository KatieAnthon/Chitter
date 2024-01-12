from lib.user import User
class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        print(rows)
        all_rows = []

        for row in rows:
            item = User(row['name_of_user'], row['email_address'], row['username'], row['user_password'], row['logged_in_status'])
            all_rows.append(item)
        
        return all_rows



        