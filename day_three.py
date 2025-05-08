# - DAY THREE 
#   1. Control Flow 
#   2. Functions

# CONTROL FLOW  - it a way to control the flow of a program.

# 1. IF STATEMENT - a conditional statement that executes a block of code if the condition is true.
# Example:
age = 18

if age >= 18:  # This checks if 'age' is greater than or equal to 18
    print("you are an adult")

# 2. IF-ELSE STATEMENT - an extension of the if statement that executes one block of code if the condition is true 
# and another block if it is false.

# Example:

age = 16
if age >= 18:  # This checks if 'age' is greater than or equal to 18
    print("you are an adult")
else:
    print("you are a minor")

# 3. ELIF STATEMENT - short for "else if", it allows you to check multiple conditions in a single if statement.
# Example:
age = 10
if age < 13:  # This checks if 'age' is less than 13
    print("you are a child")
elif age < 18:
    print("you are a teenager")
elif age < 65:
    print("you are an adult")
else:
    print("you are an old person")

# 4. NESTED IF STATEMENT - an if statement inside another if statement.
# Example:
age = 20
if age >= 18:  # This checks if 'age' is greater than or equal to 18
    print("you are an adult")
    if age >= 65:  # This checks if 'age' is greater than or equal to 65
        print("you are an old person")
    else:
        print("you are a young adult")
else: 
    print("you are a minor")

# 5. SWITCH CASE STATEMENT - a control statement that allows you to execute different blocks of code based on the value of a variable.
# Example: ?? (PAUSE ON THIS)

# 6. WHILE LOOP - a control flow statement that allows code to be executed repeatedly based on a given boolean condition.
# Example:
count = 0
while count <= 5:  # This checks if 'count' is less than 5
    print("Count:", count)  # This prints the current value of 'count'
    count += 1  # This increments 'count' by 1 count = count + 1 


# 7. FOR LOOP - a control flow statement that allows code to be executed repeatedly for a fixed number of times.
# Example:
students = ["John", "Jane", "Jim", "Jack"]  # This is a list of student names
# for i in range(5):  # This iterates 'i' from 0 to 4
#     print("Iteration:", i)  # This prints the current value of 'i'

for student in students:
    print("Student:", student)  # This prints the current student name
    # print("Student:", students[i])  # This prints the current student name using index
    # i += 1  # This increments 'i' by 1

# 8. BREAK STATEMENT - a control statement that terminates the loop and transfers control to the statement following the loop.
# Example:
for i in range(5):  # This iterates 'i' from 0 to 4
    if i == 3:  # This checks if 'i' is equal to 3
        break  # This breaks out of the loop
    print("Iteration:", i)  # This prints the current value of 'i'

# 9. CONTINUE STATEMENT - a control statement that skips the current iteration of the loop and continues with the next iteration.
# Example:
for i in range(5):  # This iterates 'i' from 0 to 4
    if i == 3:  # This checks if 'i' is equal to 3
        continue  # This skips the current iteration
    print("Iteration TWO:", i)  # This prints the current value of 'i'

# 10. PASS STATEMENT - a null statement that is used when a statement is required syntactically but you do not want to execute any code.
# Example:
for i in range(5):  # This iterates 'i' from 0 to 4
    if i == 3:  # This checks if 'i' is equal to 3
        pass  # This does nothing and continues with the next iteration
    print("Iteration THREE:", i)  # This prints the current value of 'i'


# FUNCTIONS - a block of code that only runs when it is called. You can pass data, known as parameters, into a function.
# A function can return data as a result.
# 1. FUNCTION DEFINITION - a block of code that performs a specific task.
# Example:
def greet(name):  # This defines a function named 'greet' that takes one parameter 'name'
    print("Hello, " + name)  # This prints a greeting message with the name

# 2. FUNCTION CALL - a statement that calls a function to execute its code.
greet("John")  # This calls the 'greet' function with the argument "John"

# 3. FUNCTION RETURN - a statement that returns a value from a function.
def add(a, b):  # This defines a function named 'add' that takes two parameters 'a' and 'b'
    return a + b  # This returns the sum of 'a' and 'b'
result = add(5, 3)  # This calls the 'add' function with the arguments 5 and 3 and stores the result in 'result'
print("Sum:", result)  # This prints the result of the addition

# 4. FUNCTION PARAMETERS - variables that are passed to a function when it is called.
def multiply(a, b):  # This defines a function named 'multiply' that takes two parameters 'a' and 'b'
    return a * b  # This returns the product of 'a' and 'b'
result = multiply(5, 3)  # This calls the 'multiply' function with the arguments 5 and 3 and stores the result in 'result'
print("Product:", result)  # This prints the result of the multiplication

# 5. FUNCTION ARGUMENTS - values that are passed to a function when it is called.
def divide(a, b):  # This defines a function named 'divide' that takes two parameters 'a' and 'b'
    return a / b  # This returns the quotient of 'a' and 'b'
result = divide(10, 2)  # This calls the 'divide' function with the arguments 10 and 2 and stores the result in 'result'
print("Quotient:", result)  # This prints the result of the division

