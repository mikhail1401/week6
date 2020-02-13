def greet(name):
    print(f"WELCOME TO PARTY, {name}!!!")

def talk(name):
    print(f"Hey, {name}! How are you?")

def invite_to_dinner():
    print(f"We are having a dinner tonight. Please come over.")

def goodbye(name, score):
    print(f"Thanks for comings, see you next time, {name}.")
    if score > 5:
        return True
    else:
        return False


def test_review_dinner():
    greet("John")
    talk("John")
    invite_to_dinner()
    satisfied = goodbye("John", 6)
    assert satisfied == True

def test_review_dinner_negative():
    greet("John")
    talk("John")
    invite_to_dinner()
    assert goodbye("John", 4) == True

""" 
pytest -v -s    -executes everything
pytest -v -s pytest_examples/test_examples.py   -executes only one file
pytest -v -s pytest_examples/test_examples.py::test_review_dinner   -executes specific function in the file
"""

