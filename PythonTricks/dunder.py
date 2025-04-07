# Review of dunder (double underscore) Python methods
# Credit: Tech with Time https://www.youtube.com/watch?v=qqp6QN20CpE
# Special reserved Python methods that map to somke sort of behavior
# Everything created in Python is really an object
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

