

class User():
    def __init__(self, name_of_user, email_address, username, user_password, logged_in_status):
        self.name_of_user = name_of_user 
        self.email_address = email_address
        self.username = username
        self.user_password = user_password
        self.logged_in_status = logged_in_status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.name_of_user}, {self.email_address}, {self.username}, {self.user_password}, {self.logged_in_status})"