# - DAY TWO
#     1. variables - a container for storing data values
#     2. primitive and non-primitive data types 
#     3. operators

# VARIABLES - a container for storing data values
# How can we create a variable?
# In Python, we can create a variable by simply assigning a value to it using the equals sign (=).
# For example:
name = "John Doe"  # This creates a variable named 'name' and assigns it the value "John Doe"

print(name)  # This will print the value of the variable 'name'

# PRIMITIVE DATA TYPES - is a basic data type that is not composed of other data types
# 1. int - integer
age = 25  # This creates a variable named 'age' and assigns it the value 25 (an integer)
print(age)  # This will print the value of the variable 'age'

# 2. float - floating point number
height = 5.9  # This creates a variable named 'height' and assigns it the value 5.9 (a float)
print(height)  # This will print the value of the variable 'height'

# 3. str - string
name = "John Doe"  # This creates a variable named 'name' and assigns it the value "John Doe" (a string)
print(name)  # This will print the value of the variable 'name'

# 4. bool - boolean
is_student = True  # This creates a variable named 'is_student' and assigns it the value True (a boolean)
print(is_student)  # This will print the value of the variable 'is_student'

# NON-PRIMITIVE DATA TYPES - is a data type that can store multiple values or complex data structures
# 1. list - a collection of items
fruits = ["apple", "banana", "cherry"]  # This creates a list named 'fruits' with three items
print(fruits)  # This will print the list of fruits

# 2. tuple - a collection of items that cannot be changed
fruits_tuple = ("apple", "banana", "cherry")  # This creates a tuple named 'fruits_tuple' with three items
print(fruits_tuple)  # This will print the tuple of fruits

# 3. set - a collection of unique items
fruits_set = {"apple", "banana", "cherry"}  # This creates a set named 'fruits_set' with three unique items
print(fruits_set)  # This will print the set of fruits

# 4. dictionary - a collection of key-value pairs
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}  # This creates a dictionary named 'fruits_dict' with three key-value pairs
print(fruits_dict)  # This will print the dictionary of fruits

# 5. range - a sequence of numbers
numbers_range = range(1, 10)  # This creates a range object named 'numbers_range' from 1 to 9
print(list(numbers_range))  # This will print the list of numbers from 1 to 9


# OPERATORS - symbols that perform operations on variables and values
# 1. Arithmetic Operators
# Addition
a = 5
b = 3
sum_result = a + b  # This adds the values of 'a' and 'b'
print("Sum:", sum_result)  # This will print the sum of 'a' and 'b'

# Subtraction
sub_result = a - b  # This subtracts the value of 'b' from 'a'
print("Subtraction:", sub_result)  # This will print the result of the subtraction

# Multiplication
mul_result = a * b  # This multiplies the values of 'a' and 'b'
print("Multiplication:", mul_result)  # This will print the result of the multiplication

# Division
div_result = a / b  # This divides the value of 'a' by 'b'
print("Division:", div_result)  # This will print the result of the division

# Modulus
mod_result = a % b  # This calculates the remainder of 'a' divided by 'b'
print("Modulus:", mod_result)  # This will print the result of the modulus operation

# Exponentiation
exp_result = a ** b  # This raises 'a' to the power of 'b'
print("Exponentiation:", exp_result)  # This will print the result of the exponentiation

# Floor Division
floor_div_result = a // b  # This performs floor division of 'a' by 'b'
print("Floor Division:", floor_div_result)  # This will print the result of the floor division

# 2. Comparison Operators
# Equal to
is_equal = (a == b)  # This checks if 'a' is equal to 'b'
print("Is Equal:", is_equal)  # This will print the result of the equality check

# Not equal to
is_not_equal = (a != b)  # This checks if 'a' is not equal to 'b'
print("Is Not Equal:", is_not_equal)  # This will print the result of the inequality check

# Greater than
is_greater = (a > b)  # This checks if 'a' is greater than 'b'
print("Is Greater:", is_greater)  # This will print the result of the greater than check

# Less than
is_less = (a < b)  # This checks if 'a' is less than 'b'
print("Is Less:", is_less)  # This will print the result of the less than check

# Greater than or equal to
is_greater_equal = (a >= b)  # This checks if 'a' is greater than or equal to 'b'
print("Is Greater or Equal:", is_greater_equal)  # This will print the result of the greater than or equal to check

# Less than or equal to
is_less_equal = (a <= b)  # This checks if 'a' is less than or equal to 'b'
print("Is Less or Equal:", is_less_equal)  # This will print the result of the less than or equal to check

# 3. Logical Operators
# AND (&&)
is_and = (a > 0 and b > 0)  # This checks if both 'a' and 'b' are greater than 0
print("Logical AND:", is_and)  # This will print the result of the logical AND operation

# OR (||)
is_or = (a > 0 or b < 0)  # This checks if either 'a' is greater than 0 or 'b' is less than 0   
print("Logical OR:", is_or)  # This will print the result of the logical OR operation

# NOT (!)
is_not = not (a > 0)  # This checks if 'a' is not greater than 0
print("Logical NOT:", is_not)  # This will print the result of the logical NOT operation

# 4. Assignment Operators
# Assignment
x = 10  # This assigns the value 10 to the variable 'x'
print("Assignment:", x)  # This will print the value of 'x'

# Add and assign
x += 5  # This adds 5 to the current value of 'x' and assigns the result back to 'x'
print("Add and Assign:", x)  # This will print the updated value of 'x'

# Subtract and assign
x -= 3  # This subtracts 3 from the current value of 'x' and assigns the result back to 'x'
print("Subtract and Assign:", x)  # This will print the updated value of 'x'

# Multiply and assign
x *= 2  # This multiplies the current value of 'x' by 2 and assigns the result back to 'x'
print("Multiply and Assign:", x)  # This will print the updated value of 'x'

# Divide and assign
x /= 4  # This divides the current value of 'x' by 4 and assigns the result back to 'x'
print("Divide and Assign:", x)  # This will print the updated value of 'x'

# 5. Identity Operators  - (ASSIGNMENT OPERATORS)