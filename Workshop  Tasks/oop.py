class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False
# Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Method to wake up wolf (self needs to be passed as argument so
# that all of the properties are available to the method)
    def wake_up(self):
        self.is_sleeping = False


T.B.C in email.py