# python-basics upcoming class notes.
40. Python Object oriented programming.

Object is instance of class. by using programming we can create representations of real-life objects
attributes = is/has Ex: Name, age, height
methods = actions Ex: eat, sleep, make youtube videos.
In order to create a object, we need to create a class.
A class can function as a blueprint that will describe what attributes and methods that our distinct type of object will have you can either create class within your main module, or you can create seperate file dedicated solely for you class.
if class is large you may want to consider placing your class within a separte module
Syntax:
class Car:

41. Class Variables
init method is also known as constructor
There is a difference between class and instance variables. An instance variable is defined inside of a constructor and they can be given unique values. With class variables they are declared within in a class but outside the constructor and we can set a default value for all instances of this class for all unique objects that are created and you can change those values later too.
**Class variable is defined inside the class and outside the constructor.

42. Inheritence in Python.
Inheritence means to receive derive or be left with and we can apply this concept to programming.
classes can inherit something usually attributes and methods from another class these classes can from partent-child relationships where a child will receive eveyrthing that the parent class has much like you inherit jeans from your parents.

With the help of inheritence no need to copy the code.
each child class can have their own unique attributes and methods as well along with the attibutes and methods of that they inherit from their parent.

43. Multi-level inheritence in python.
multi-level inheritence is when a derived (child) class inherits another derived (child) class.

44. multiple inheritence is when a child class is derived from more than one parent class.

45. Method over riding in python.
method overriding is the ability of an object oriented programming languageto allow a subclass also known as child class to provide a specific implementation of a method that is already provided by one of its parents.

46. Method Chaining.
**method chaining is calling multiple methods sequentially. 
**each call performs an action on the same object and returns self.
syntax:
car = Car()
car.turn_on().drive()
car.turn_on()\
.drive()\
.break()\
.turn_off()

47. Super function 
super function is used to give access to methods of a parent class.
reurtns a temporary object of a parent class when used.
syntax:
super()

48. Abstract Classes in python.
**prevents a user from creating an object of that class
** also compels a user to override abstract methods in a child class.
** abstract class is a class which contains one or more abstract methods.
**abstact method is a methond that has a declaration but does not have an implementation.





