
class Peep():
    def __init__(self, peep_text, user_id):
        self.peep_text = peep_text
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep({self.peep_text}, {self.user_id})"