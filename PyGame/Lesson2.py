'''
Lesson 2: Introduction to Object Oriented Programming (OOP)

What is OOP?

OOP is a computer programming model that organizes software design around objects. An object can be defined as a data that has unique attributes and behaviors. You can relate this to dictionaries or JSON, where each key has a specific value.

What is a Class?

You can think of class as a template to create objects that provide different attributes also known as properties. Classes also provide methods which implement a specific behavior on a given object.

What are Properties?

You can think properties as variable that give objects different characteristics therefore making them unique.

What are Methods?

Methods are what we usually know as functions. We call these functions inside of classes methods because they can be called on objects that are created under a class and operate on data that is contained within the class.

A function on the other hand is a piece of code that is called by its name and can accept data (parameters) and optionally return data.

In other words, a method is on an object whereas a function is independent of an object.
'''

class Person:
    name = "John"
    age = 17

    # Place 2 underscores in front and behind init
    def __init__(self, name, age):
        '''
        Self Paramenter is a reference to the current instance of the class which is used to access different variables of the class such as name and age.
        '''
        self.name = name
        self.age = age

    def hello(self):
        print("Hi my name is", self.name, "and I am", self.age, "years old.")

p1 = Person("Alex", 15)
p2 = Person("Sarah", 16)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
