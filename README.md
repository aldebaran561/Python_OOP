<<<<<<< HEAD:OOP.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Object Oriented Programming\n",
    "\n",
    "Python is a multi-paradigm programming language. It supports different programming approaches. One of the most popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).\n",
    "\n",
    "An object has two characteristics:\n",
    "\n",
    "- attributes\n",
    "- behavior\n",
    "\n",
    "Let's see a brief example:\n",
    "\n",
    "A car has attributes like the color, number of doors, model, year, among others. But also, the sema car has some behaviors, like accelerating, braking, turning left or right and reversing.\n",
    "\n",
    "## Class\n",
    "\n",
    "A class is a blueprint that defines the variables and the methods (attributes and behaviors) common to all objects of a certain kind. You can define a class in Python using ```class``` statement.\n",
    "\n",
    "```python\n",
    "class Car:\n",
    "    pass\n",
    "```\n",
    "\n",
    "### Constructors\n",
    "\n",
    "The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. As it's said before, this is necessary to define the attributes of the class. In Python the ```__init__()``` method is called the constructor and is always called when an object is created.\n",
    "\n",
    "```python\n",
    "class Car:\n",
    "    \n",
    "    def __init__(self, model, color):\n",
    "        self.model = model\n",
    "        self.color = color\n",
    "    \n",
    "ferrari = Car(2021,'Green')\n",
    "audi = Car(2019, 'Black')\n",
    "```\n",
    "\n",
    "Note that the ```self``` statement is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in Python.\n",
    "\n",
    "### Class and Instance Variables\n",
    "\n",
    "In Python, instance variables are variables whose value is assigned inside a constructor or method with self. \n",
    "\n",
    "```python\n",
    "class Car:\n",
    "    \n",
    "    style = 'sports car' # class Variable\n",
    "    \n",
    "    def __init__(self, model, color):\n",
    "        self.model = model #instance variable \n",
    "        self.color = color #instance variable\n",
    "\n",
    "ferrari = Car(2007,'Red')\n",
    "ferrari.style\n",
    "```\n",
    "\n",
    "## Pillars of OOP\n",
    "\n",
    "The four pillars of object-oriented programming are:\n",
    "\n",
    "- Abstraction.\n",
    "- Encapsulation.\n",
    "- Inheritance.\n",
    "- Polymorphism.\n",
    "\n",
    "### Abstraction\n",
    "\n",
    "Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that **\"what function does\"** but they don't know **\"how it does.\"**\n",
    "\n",
    "### Encapsulation\n",
    "\n",
    "It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method.\n",
    "\n",
    "#### Access modifiers\n",
    "\n",
    "- Public: The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default.\n",
    "- Protected: Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.\n",
    "- Private: The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.\n",
    "\n",
    "#### Getters and Setters\n",
    "\n",
    "Basically, the main purpose of using getters and setters is to ensure data encapsulation. Getters and Setters in python are often used when:\n",
    "\n",
    "- We use getters & setters to add validation logic around getting and setting a value.\n",
    "- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.\n",
    "\n",
    "```python\n",
    "class id:\n",
    "\n",
    "    def __init__(self, id_number):\n",
    "        self.__id_number = id_number\n",
    "\n",
    "    #getter\n",
    "    def get_id(self):\n",
    "        return self.__id_number\n",
    "\n",
    "    #setter\n",
    "    def set_id(self, id_number):\n",
    "        self.__id_number = id_number\n",
    "\n",
    "victor = id(1020321435)\n",
    "print(victor.get_id())\n",
    "victor.set_id(1923214872)\n",
    "print(victor.get_id())\n",
    "\n",
    "```\n",
    "\n",
    "### Inheritance\n",
    "\n",
    "Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).\n",
    "\n",
    "### Polymorphism\n",
    "\n",
    "Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).\n",
    "\n",
    "Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Methods in Python\n",
    "\n",
    "At first, it is a little confusing the statement used in class, for example, when it is correct to use ```self``` or ```class```. So here's a brief explanaition:\n",
    "\n",
    "- Static Methods: This type of method takes neither a ```self``` nor a ```cls``` parameter, but  it’s free to accept an arbitrary number of other parameters, if it's needed. Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.\n",
    "\n",
    "    Before a static method it is common to use a decorator ```@staticmethod```\n",
    "    \n",
    "    ```python\n",
    "    class Calculo:\n",
    "\n",
    "        @staticmethod #Decorator\n",
    "        def potencia(r): #This is a static method\n",
    "            return r ** 2\n",
    "    ```\n",
    "\n",
    "    This kind of method\n",
    "\n",
    "     - Can't modify object instance state\n",
    "     - Can't modify class state\n",
    "\n",
    "- Class Methods: Instead of accepting a self parameter, class methods take a ```cls``` parameter that points to the class—and not the object instance—when the method is called. Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.\n",
    "\n",
    "    Before a class methods it is common to use a decorator ```@classmethod```\n",
    "    \n",
    "    ```python\n",
    "    class MethodTypes:\n",
    "\n",
    "        name = \"Ragnar\"\n",
    "\n",
    "        def instanceMethod(self):\n",
    "            self.lastname = \"Lothbrock\"\n",
    "            print(self.name)\n",
    "            print(self.lastname)\n",
    "\n",
    "        @classmethod #Decorator\n",
    "        def classMethod(cls): #This is a class method\n",
    "            cls.name = \"Lagertha\"\n",
    "            print(cls.name)\n",
    "    ```\n",
    "    \n",
    "    This kind of method\n",
    "\n",
    "     - Can't modify object instance state\n",
    "     - Can modify class state\n",
    "    \n",
    "- Instance Methods: Instance methods are the most common type of methods in Python classes. Instance methods must have ```self``` as a parameter, but you don't need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won't be able to access them without going through self.\n",
    "\n",
    "    ```python\n",
    "    class Parrot:\n",
    "\n",
    "        def fly(self): #This is a instance method\n",
    "            print(\"Parrot can fly\")\n",
    "    ```\n",
    "    \n",
    "    This kind of method\n",
    "\n",
    "     - Can modify object instance state\n",
    "     - Can modify class state"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
=======
# Object Oriented Programming

Python is a multi-paradigm programming language. It supports different programming approaches. One of the most popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

- attributes
- behavior

Let's see a brief example:

A car has attributes like the color, number of doors, model, year, among others. But also, the sema car has some behaviors, like accelerating, braking, turning left or right and reversing.

## Class

A class is a blueprint that defines the variables and the methods (attributes and behaviors) common to all objects of a certain kind. You can define a class in Python using ```class``` statement.

```python
class Car:
    pass
```

### Constructors

The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. As it's said before, this is necessary to define the attributes of the class. In Python the ```__init__()``` method is called the constructor and is always called when an object is created.

```python
class Car:
    
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
ferrari = Car(2021,'Green')
audi = Car(2019, 'Black')
```

Note that the ```self``` statement is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in Python.

### Class and Instance Variables

In Python, instance variables are variables whose value is assigned inside a constructor or method with self. 

```python
class Car:
    
    style = 'sports car' # class Variable
    
    def __init__(self, model, color):
        self.model = model #instance variable 
        self.color = color #instance variable

ferrari = Car(2007,'Red')
ferrari.style
```

## Pillars of OOP

The four pillars of object-oriented programming are:

- Abstraction.
- Encapsulation.
- Inheritance.
- Polymorphism.

### Abstraction

Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that **"what function does"** but they don't know **"how it does."**

### Encapsulation

It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method.

#### Access modifiers

- Public: The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default.
- Protected: Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
- Private: The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.

#### Getters and Setters

Basically, the main purpose of using getters and setters is to ensure data encapsulation. Getters and Setters in python are often used when:

- We use getters & setters to add validation logic around getting and setting a value.
- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

```python
class id:

    def __init__(self, id_number):
        self.__id_number = id_number

    #getter
    def get_id(self):
        return self.__id_number

    #setter
    def set_id(self, id_number):
        self.__id_number = id_number

victor = id(1020321435)
print(victor.get_id())
victor.set_id(1923214872)
print(victor.get_id())

```

### Inheritance

Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

### Polymorphism

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

## Methods in Python

At first, it is a little confusing the statement used in class, for example, when it is correct to use ```self``` or ```class```. So here's a brief explanaition:

- Static Methods: This type of method takes neither a ```self``` nor a ```cls``` parameter, but  it’s free to accept an arbitrary number of other parameters, if it's needed. Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

    Before a static method it is common to use a decorator ```@staticmethod```
    
    ```python
    class Calculo:

        @staticmethod #Decorator
        def potencia(r): #This is a static method
            return r ** 2
    ```

    This kind of method

     - Can't modify object instance state
     - Can't modify class state

- Class Methods: Instead of accepting a self parameter, class methods take a ```cls``` parameter that points to the class—and not the object instance—when the method is called. Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

    Before a class methods it is common to use a decorator ```@classmethod```
    
    ```python
    class MethodTypes:

        name = "Ragnar"

        def instanceMethod(self):
            self.lastname = "Lothbrock"
            print(self.name)
            print(self.lastname)

        @classmethod #Decorator
        def classMethod(cls): #This is a class method
            cls.name = "Lagertha"
            print(cls.name)
    ```
    
    This kind of method

     - Can't modify object instance state
     - Can modify class state
    
- Instance Methods: Instance methods are the most common type of methods in Python classes. Instance methods must have ```self``` as a parameter, but you don't need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won't be able to access them without going through self.

    ```python
    class Parrot:

        def fly(self): #This is a instance method
            print("Parrot can fly")
    ```
    
    This kind of method

     - Can modify object instance state
     - Can modify class state
>>>>>>> c9cc9beea763631fe9dcbe1041dac0e630cd9041:README.md
