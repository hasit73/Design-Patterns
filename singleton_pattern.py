"""
Singleton Pattern:

Make sure that only one instance will be created of class
Helpful when providing global access of shared object.

Singleton pattern is one of the simplest design patterns.
This type of design pattern comes under creational pattern as 
this pattern provides one of the best ways to create an object.
"""


class Person:
    """ Person class have properties like name, age """

    # global instance maintain copy of created instance
    __instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(__class, name, age):
        """ Whenever new object created this method invoke
            and prevent to generate new instances if already exists
        """
        # is instance is None means no object created yet.
        if Person.__instance is None:
            Person.__instance = object.__new__(__class)
        return Person.__instance

    def get_name(self):
        """ Get name of person object """
        return self.name


if __name__ == "__main__":

    # create two objects
    p1 = Person("Roy", 34)
    p2 = Person("Riya", 28)

    # check reference of both
    # it should be same because we need single instance.
    print("Id of person object 1: ", id(p1))
    print("Id of person object 2: ", id(p2))

    # check whether both variable pointing to the same
    # reference location of not
    print("Is person object 1 is object 2: ", p1 is p2)
