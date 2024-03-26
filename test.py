# This is a sample Python script with various syntax examples.

# Imports
import math
import os

# Variables and Data Types
integer_example = 42
float_example = 3.14
string_example = "Hello, Python!"
boolean_example = True
list_example = [1, 2, 3, 4, 5]
tuple_example = (6, 7, 8, 9, 10)
dict_example = {'key1': 'value1', 'key2': 'value2'}
set_example = {11, 12, 13, 14, 15}

# Printing and String Formatting
print("Basic printing:", string_example)
print(f"Formatted string: {integer_example} and {float_example}")
print("Multiple items:", string_example, integer_example)

# Control Structures
if boolean_example:
    print("Boolean is true!")
else:
    print("Boolean is false!")

for item in list_example:
    print("List item:", item)

for key, value in dict_example.items():
    print(f"Dict item: {key} = {value}")

i = 0
while i < 5:
    print("While loop, i =", i)
    i += 1

# Functions
def example_function(param1, param2):
    return param1 + param2

print("Function output:", example_function(3, 4))

# List Comprehension
squared_list = [x ** 2 for x in list_example]
print("Squared list:", squared_list)

# Classes and Objects
class ExampleClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

example_object = ExampleClass("An example object")
print("Object value:", example_object.get_value())

# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Divided by zero!")
finally:
    print("This is executed no matter what.")

# Working with Files
with open('example.txt', 'w') as f:
    f.write("Writing to an example file.")

with open('example.txt', 'r') as f:
    content = f.read()
print("File content:", content)

# Using Imported Modules
print("Pi from math module:", math.pi)
print("Current working directory:", os.getcwd())

# Dictionaries and Set Operations
new_dict = {i: i * 2 for i in range(5)}
print("New dict with comprehension:", new_dict)

union_set = set_example | {16, 17, 18}
print("Union of sets:", union_set)

# Lambda Functions
square = lambda x: x * x
print("Square of 5:", square(5))

# Working with Enums (Python 3.4+)
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(f"\nEnum example:", Color.RED)

x = 100
y = 100 + x

# End of the Python syntax examples file

