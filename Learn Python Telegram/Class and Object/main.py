# What is a class in Python?
#
# A class is like a blueprint or template for creating
# objects. It defines the properties (data) and
# behaviors (actions) that the objects will have.
#
# Think of a Car
# - A class is the idea of a car. It defines what all cars
#   have (like brand, model, year) and what they can do
#   (like start, stop).
# - An object is a real car made using this blueprint, 
#   like a Tesla o Ferrari.

# Define Python Class
# We use the Class Keyword to create a class in python

# class ClassName:
#    # Class Definition

class Car:
    brand = "BMW" # Class attribute
    model = "X5"  # Class attribute
    year  = 2023  # Class attribute

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Objects in Python
# An object is a specific instance of a class. It contains 
# the data and behavior defined in the class.

# Syntax to Create an Object

# Creating an object of the Car class

my_car = Car()

my_car.display_info()

# Access Class Attributes Using Objects
# In Python, you can access class-level attributes
# directly using dot notation on the class itself.

# Accessing class attributes directly using dot notation.

print(Car.brand)

# - Car.brand: Accesses the brand attribute directly from the class,
#   without needing an object.

print(Car.model)

# - Class-level Attributes: These attributes belong to the class
#   itself and are shared across all instances of the class.

# Class and Object in One Simple Example

# Defining the Book class
class Book:
    # The __init__ method is called when an object is created
    # It initializes the object's attributes
    def __init__(self, title, author, pages):
        self.title = title      # Attribute: the book's title
        self.author = author    # Attribute: the book's author
        self.pages = pages      # Attribute: number of pages

    # A method to display information about the book
    def display_info(self):
        print(f"Title: '{self.title}', Author: {self.author}, Pages: {self.pages}")

    # Another method: an action the book can conceptually do
    def open_to_page(self, page_number):
        if 0 < page_number <= self.pages:
            print(f"Opening '{self.title}' to page {page_number}.")
        else:
            print(f"Page {page_number} is out of range for '{self.title}'.")

# Creating an object 'my_fav_book' from the Book class
my_fav_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)

# Creating another object 'another_book'
another_book = Book("1984", "George Orwell", 328)

# Accessing attributes and calling methods
print(my_fav_book.author)       # Outputs: Douglas Adams
my_fav_book.display_info()      # Outputs: Title: 'The Hitchhiker's Guide to the Galaxy', Author: Douglas Adams, Pages: 224
another_book.open_to_page(101)  # Outputs: Opening '1984' to page 101.
my_fav_book.open_to_page(300)   # Outputs: Page 300 is out of range for 'The Hitchhiker's Guide to the Galaxy'.

# Book is the class (blueprint).
# my_fav_book is an object (instance) created from the class.
# Dot notation (my_fav_book.attribute) accesses the properties and methods of the object.

# Create Multiple Objects of Python Class
# We can also create multiple objects from a single class.

# Defining the Coche class

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def despliega_informacion(self):
        print(f"{self.marca} {self.modelo}")

    def arranca_motor(self):
        print("El motor ha arrancado!")

# Creating multiple objects from the Coche class

coche1 = Coche("BMW", "X5")
coche2 = Coche("Audi", "A4")
coche3 = Coche("Mercedes", "C-Class")

# Accessing object properties and methods.

coche1.despliega_informacion()
coche2.despliega_informacion()
coche3.despliega_informacion()

# Calling the method

coche3.arranca_motor()

# arranca_motor() is a method in the Coche class.

# we create an object coche3 and call the method using dot notation.
        