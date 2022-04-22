'''
    Even or Odd 8kyu challenge on CodeWars 
    Create a function that takes an integer as an argument and
    returns "Even" for even numbers or "Odd" for odd numbers.
    Stretch goal: Make it a class and do testing. Add two to the number
'''
#A person who wants to find out the even and odds number in their life. 
class Person:
    def __init__(self, name, number):   #Constructor takes two argument and gives self is the new instance object 
        self.name = name                # Initiates instance object
        self.number = number            # Instance object's favourite number
    def even_or_odd(self):              #This is a method that contains two arguements.
        if self.number % 2 == 0:
            return "Even"
        else:
            return "Odd"

if __name__ == '__main__': # When run for testing only
    # self-test code
    bob = Person('Bob Smith', 24)
    print(bob.even_or_odd())


