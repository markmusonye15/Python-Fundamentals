# - DAY FOUR
#     3. Data structures 

# Data Structures - a way to organize and store data in a computer so that it can be accessed and modified efficiently

# 1 . List - a collection of items that can be changed
# Example:
fruits = ["apple", "banana", "cherry", "Orange"]  # This creates a list named 'fruits' with three items
my_list = [1, True, "apple", 3.14, { "name": "John Doe"}]  # This creates a list named 'my_list' with four items of different data types
print(fruits)  # This will print the list of fruits
print(my_list)  # This will print the list of mixed data types

#  Indexing - accessing elements in a list using their index (0 - Nth index)
print(fruits[1])

# slicing - accessing a range of elements in a list using their index
print("Slicing", fruits[2:3:3]) # LOOK INTO THIS

# Adding elements to a list
fruits.append("orange")  # This adds "orange" to the end of the list 'fruits'
print(fruits)  # This will print the updated list of fruits

# Adding elements to the beginning of a list
fruits.insert(2, "grape")  # This adds "grape" to the beginning of the list 'fruits'
print(fruits)  # This will print the updated list of fruits

# Removing elements from a list
fruits.remove("banana")  # This removes "banana" from the list 'fruits'
print(fruits)  # This will print the updated list of fruits

# Removing elements from the beginning of a list
fruits.pop(3)  # This removes the first element from the list 'fruits'
print(fruits)  # This will print the updated list of fruits


# 2. Tuple - a collection of items that cannot be changed
#Example 
fruits_tuple = ("apple", "banana", "cherry", "oranges", "beetroots", "pinapples")  # This creates a tuple named 'fruits_tuple' with three items
print(fruits_tuple)  # This will print the tuple of fruits
print(fruits_tuple[1])  # This will print the second item in the tuple
print(fruits_tuple[1:3])  # This will print the second and third items in the tuple
print(fruits_tuple[1:3:2])  # This will print the second and third items in the tuple

# fruits_tuple[1] = "orange"  # This will raise an error because tuples cannot be changed


# 3. Set - a collection of unique items
# Example
fruits_set = {"apple", "banana", "cherry", "orange", "banana", "apple", "orange"}  # This creates a set named 'fruits_set' with three unique items
print(fruits_set)  # This will print the set of fruits

# Adding elements to a set
fruits_set.add("grape")  # This adds "grape" to the set 'fruits_set'
print(fruits_set)  # This will print the updated set of fruits

# Removing elements from a set
fruits_set.remove("banana")  # This removes "banana" from the set 'fruits_set'
print(fruits_set)  # This will print the updated set of fruits

# 4. Dictionary - a collection of key-value pairs (Objects)
# Example
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}  # This creates a dictionary named 'fruits_dict' with three key-value pairs
print(fruits_dict)  # This will print the dictionary of fruits

students = {"Emma Karanja": {
    "age": 23,
    "gender": "Female",
    "course": "Software Engineering",
    "year": 2025,
    "email": "emma@gmail.com"
}, "Catherine Henu": "3457746387"}
print(students["Emma Karanja"])


# Adding elements to a dictionary
fruits_dict["orange"] = 4  # This adds a new key-value pair "orange": 4 to the dictionary 'fruits_dict'
print(fruits_dict)  # This will print the updated dictionary of fruits

# Removing elements from a dictionary
del fruits_dict["banana"]  # This removes the key-value pair "banana": 2 from the dictionary 'fruits_dict'
print(fruits_dict)  # This will print the updated dictionary of fruits

# 5. Range - a sequence of numbers
# Example
numbers_range = range(1, 10)  # This creates a range object named 'numbers_range' from 1 to 9
print(list(numbers_range))  # This will print the list of numbers from 1 to 9

# length of a dictionary
print(len(fruits_dict))  # This will print the length of the dictionary 'fruits_dict'
