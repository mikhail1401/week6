# Model

class Welcome():

    def __init__(self, name):
        self.name = name
        print(f"Respect {self.name}")
    def greet_guests(self, names: list, *args: str) -> int:
        """ Function loops through the names and adds welcome message, and just prints all args passed"""

        fee = 100
        print("================ GREETING THE GUESTS ============")
        for name in names:
            print(f"Hello, {name}! Welcome to our party!")
        print("=================== ARGS ===============")
        for arg in args:
            if type(arg) == str:
                print(f"arguments:{arg.title()}")
            elif type(arg) != str:
                arg = str(arg)
                print(f"arguments:{arg}")
        print(f"I love you {self.name}")


    def greet_guests2(self, names: list, *args: str):
        """ Function loops through the names and adds welcome message, and just prints all args passed"""

        print("================ GREETING THE GUESTS ============")
        for name in names:
            print(f"Hello, {name}! Welcome to our party!")
        print("=================== ARGS ===============")
        for arg in args:
            if type(arg) == str:
                print(f"arguments:{arg.title()}")
            elif type(arg) != str:
                arg = str(arg)
                print(f"arguments:{arg}")
        
        return 'hello'


class CoolWelcome(Welcome):
    
    def cool_guests_greet(self, names: list):
        for name in names:
            print(f"Yooooo. {name}! Brooo, wazuuup!")



# data   
guests = ['Nicolas Cage', 'Julia Roberts', 'Eddie Murphy', 'Madonna']
cool_guests = ['50 cent', 'Marshal Mathew', 'Justin T']

#execution
obj1 = Welcome('Amelie Lens')
print(f"\n1st execution")
Welcome('Amelie Lens').greet_guests(guests, 'plov', 'kebab', 'vegan salad', 'protein shakes', 5)
print(f"\n2nd execution")
obj1.greet_guests(guests, 'plov', 'kebab', 'vegan salad', 'protein shakes', 5)

print(f'\n3rd execution')
CoolWelcome('Charlotte de Witte').cool_guests_greet(cool_guests)
print(f'\n4th exectuion')
CoolWelcome('Charlotte de Witte').greet_guests(cool_guests, 'plov', 'samsa')

""" Homework
Check the chapter 10 and learn hot read the files"""