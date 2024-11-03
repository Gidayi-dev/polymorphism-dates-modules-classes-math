mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  

mystr = "banana"

for x in mystr:
  print(x)


Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)  
class MyNumbers:
      def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

#Class polymorphism
#Different classes with the same method
class Car:
      def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
  
  #Inheritance Class Polymorphism
  class Vehicle:
      def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

#Local Scope
def myfunc():
    x = 300
    print(x)
myfunc

import datetime

x = datetime.datetime.now()
print(x)

#function inside a function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
    
myfunc

#Global scope
x = 300

def myfunc():
    print(x)
myfunc

print(x)

#python modules
def greeting(name):
    print("Hello," + name)
#Now we can use the module we just created, by using the import statement
import mymodule

mymodule.greeting("Jonathan")

#Variables in Module
#in mymodule.py
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

#Import the module named mymodule, and access the person1 dictionary
import mymodule

a = mymodule.person1["age"]
print(a)

#Naming a Module
#You can name the module file whatever you like, but it must have the file extension .py
#Re-naming a module
#You can create an alias when you import a module, by using the as keyword
import mymodule as mx 

a = mx.person1["age"]
print(a)

#Built-in Modules
import platform

x = platform.system()
print(x)

#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function
import platform

x = dir(platform)
print(x)

#Import From Module
#You can choose to import only parts from a module, by using the from keyword.
def greeting(name):
      print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#Import only the person1 dictionary from the module
from mymodule import person1

print (person1["age"])
#Dates
import datetime

x = datetime.datetime.now()
print(x)

#Return the year and name of weekday
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
import datetime

x = datetime.datetime(2024, 5, 17)
print(x)

#The strftime() Method
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#Math
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)

print(x)

#The pow(x, y) function returns the value of x to the power of y (xy)
x = pow(4, 3)

print(x)

#The Math Module
import math

x = math.sqrt(64)

print(x)

#The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#The math.pi constant, returns the value of PI (3.14...)
import math

x = math.pi
print(x)