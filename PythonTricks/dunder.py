# Review of dunder (double underscore) Python methods
# Special reserved Python methods that map to somke sort of behavior

# Define behavior when a new instance of an object is created (OOP)
class Rect: 
  def __init__(self, x, y): 
    self.x = x
    self.y = y

Rect(2,3)
