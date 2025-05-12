# - DAY ONE 
#   1. OOP using python 


# OOP - Object Oriented Programming - it is more like a 
# real world programming concepts that uses a mixture of classes and objects to create a program.

#   2. Classes and Objects
# A class is a blueprint for creating objects. 
# An object is an instance of a class.

#   3. Attributes and Methods
# Attributes are the variables that belong to a class.
# Methods are the functions that belong to a class.

# How can we create a class?

class Person:
    # How can we make the objects unique?
    # Constructor
    def __init__(self, name, age, occupation, dob):
        # Attributes
        self.name = name
        self.age = age
        self.occupation = occupation
        self.dob = dob

    
    # How can I create a method within a class?
    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

# How can I create an object out of a class?

person_one = Person('John Doe', 30, 'Software Engineer', '01/01/1990')
person_two = Person('Jane Doe', 25, 'Data Scientist', '01/01/1995')

# print(person_one.name, person_one.age, person_one.occupation, person_one.dob)
# print(person_two.name, person_two.age, person_two.occupation, person_two.dob)

# person_one.greet()


#   4. Inheritance, Polymorphism, Encapsulation, Abstraction
# Inheritance - it is a way to create a new class that is a modified version of an existing class.

# can we create a class that inherits from another class?
class Student(Person):
    
    def __init__(self, name, age, occupation, dob, attendance, track):

        super().__init__(name, age, occupation, dob)

        # Attributes
        self.attendance = attendance
        self.track = track
        

    def ask_question(self):
        print(f'Hello, my name is {self.name} and I am a student. I have {self.track} attendance.')

students = []

student_one = Student('John Doe', 30, 'Software Engineer', '01/01/1990', 'Software Engineering', '90%')
students.append(student_one)
student_two = Student('Jane Doe', 25, 'Data Scientist', '01/01/1995', 'Data Science', '95%')
students.append(student_two)
student_three = Student('Jim Doe', 28, 'Data Analyst', '01/01/1992', 'Data Analysis', '85%')
students.append(student_three)

for student in students:
    print(student.name, student.age, student.occupation, student.dob, student.attendance, student.track)
    student.ask_question()
    student.greet()
    student.ask_question()
    print(f'Attendance: {student.attendance}')
    print(f'Track: {student.track}')
    print('-------------------')

