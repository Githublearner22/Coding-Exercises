''' 
    Sum of positive 8kyu challenge on CodeWars 
    
    You get an array of numbers, return the sum of all of the positives ones.
    Example [1,-4,7,12] => 1 + 7 + 12 = 20
    Note: if there is nothing to sum, the sum is default to 0.

    Stretch goal: Make it a class and do testing placed in testing file.
'''
#A dog who has a selection of bones but should only choose the good bones.
class Dog:
    def __init__(self, name, arr):  #The constructor init has 3 arguments. Self creates the new instance
        self.name = name            #This creates an instance object with name
        self.arr = arr

    def positive_sum(self): #Must use self to be able to use the instance object within
        total = 0
        for a in self.arr:
            if a > 0:
                total += a
        return total  

if __name__ == '__main__': # When run for testing only
    # self-test code
    marley = Dog('Marley', [1, 3 , 5, -7, 4])
    print(marley.positive_sum())

"""
Best Solution: 

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

This is a list comprehension is the best solution as it is less coding and 
will run substantially faster. They are twice as fast. This is because its creates a list on demand then suspending and 
resuming a function's frame. It does not need to load the append attibute.
"""
