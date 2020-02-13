# WEEK 6
02/08/2020

## Recap
- Functions 
    A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

- Package, module
    Consider a module to be the same as a code library.
    A file containing a set of functions you want to include in your application.

- OOP (Object Oriented Programming) concepts:
    -Classes
        A Class is like an object constructor, or a "blueprint" for creating objects.
    - Objects
        Almost everything in Python is an object, with its properties and methods.
        Object is simply a collection of data (variables) and methods (functions) that act on those data. And, class is a blueprint for the object.
    - Ingeritence (наследование, наследство)
        Inheritance allows us to define a class that inherits all the methods and properties from another class. (Parent class and child class).
    - method/function overriding
    - Encapsulation (hiding data >> __name)

- Polymorphism (and function overloading)
     The word polymorphism means having many forms. 
     Polymorphism means that different types respond to the same function.
     In programming, polymorphism means same function name (but different signatures) being uses for different types.
    (see examples in polymorphism.py)

-Abstraction
    - with classes, interface (blueprint of classes, just declare the functions and attributes, you don't define function (no body of the functions))


## Exception hnadling and testing your code

### Creating your tests, testing your code
Pytest, unittest etc

    Test1 (functions)
    1. precondition
    2. action
    3. verify >> generates PASS/FAIL (assert)

    Test2 (functions)
    1. precondition
    2. action
    3. verify >> generates PASS/FAIL (assert)

### Exception handling

    def functionname(arg1, arg2):
        try:
            <your main code is here>
        except ZeroDivisionError:
            <code if you face division by zero>
        except:
            <code if you have an error>


## Testing framework (Web Testing)
- How to create a project for automated web testing
 
**PYTEST**

Pytest collects all files and functions starting with 'test'