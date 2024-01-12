from lib.peep import Peep


""" test user inputs are initialised in the class"""
def test_peep_variables_are_initialised():
    peep = Peep('my first peep', 2)
    assert peep.peep_text == 'my first peep'
    assert peep.user_id == 2

""" when the same value is entered - the class recognises that it is not 2 separate items"""

def test_peep_variables_do_not_duplicate():
    peep = Peep('my first peep', 2)
    peep2 = Peep('my first peep', 2)
    assert peep == peep2

"""when returning the user input - the digested information is readable"""

def test_peep_formatting():
    peep = Peep('my first peep', 2)

    assert str(peep) == 'Peep(my first peep, 2)'

