'''
Review of dunder (double underscore) Python methods
Credit: Tech with Time https://www.youtube.com/watch?v=qqp6QN20CpE
Special reserved Python methods that map to somke sort of behavior
Everything created in Python is really an object, which allows for preexisting dunder methods to be defined

When defining any custom class, good practice to define __str__ and __repr__ (one for users, one for development)
Discusses: 
__init__()
__repr__()
__add__()
__del__()
__call__()
__mul__()
__enter__()
__exit__()
__setitem__()
'''
def func():
  pass
print(type(func))

# __init__ Define behavior when a new instance of an object is created (OOP)
class Rect: 
  def __init__(self, x, y): 
    self.x = x
    self.y = y
Rect(2,3)

# __add__ Defines behavior when two objects of same type added together
str1 = "hello"
str2 = "world"
new_str = str1 + str2 
# We take concatenation for granted, but how does Python know to add two string objects?
# There is an __add__ method defined in the String class
new_str = str1.__add__(str2) # Can call the function directly instead of using + operator 
print(new_str)

# __len__ Determines an object length (however that is defined for object class)
print(len(str1)) # Returns 5
print(str1.__len__()) # Returns 5

# __repr__ Wrapper method
class Car: 
  def __init__(self, make, model, year): 
    self.make = make
    self.model = model
    self.year = year

  # __str__ meant for user-friendly output
  def __str__(self): 
    return f"{self.year} {self.make} {self.model}"

  # __repr__ is menat for a more detailed, unambiguous output
  def __repr__(self): 
    return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

my_car = Car('Toyota', "Corolla', 2021)

print(str(my_car))   # User-friendly output: Toyota Corolla 2021
print(repr(my_car))  # Development-friendly output: Car(make='Toyota', model='Corolla', year=2021

# Tech with Tim example
def Counter: 
  def __init__(self): 
    self.value = 1
  def count_up(self): 
    self.value += 1
  def count_down(self): 
    self.value -= 1
  def __str__(self): 
    return f"Count={self.value}"
  def __add__(self, other): 
    if isinstance(other, Counter): 
      return self.value + other.value
    raise Exception("Invalid type. Needs to be type 'Counter')

count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_down()

print(count1, count2)   # Requires __str__ to be defined for this object class
print(count1 + count2)  # Requries __add__ to be defined for this object class
print(count1 + 2)  # Requries __add__ to be defined for this object class and some sort of type checking
    
