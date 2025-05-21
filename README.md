# Python Learning Project

A step-by-step learning journey through Python fundamentals.

## Overview

This repository contains code examples and notes for learning Python programming fundamentals. The content is organized by learning days, with each day focusing on specific concepts.

## Learning Progress

### Day One
- Installing Python
- Creating and running Python files
- Python comments and basic syntax

### Day Two
- Variables and their usage
- Data types (primitive and non-primitive)
- Operators (arithmetic, comparison, logical, assignment)

### Day Three
- Control Flow statements:
  - If, if-else, elif conditions
  - Nested if statements
  - While loops
  - For loops
  - Break, continue, and pass statements
- Functions:
  - Function definition and calling
  - Return values
  - Parameters and arguments

### Day Four
- Data Structures:
  - Lists (creation, indexing, slicing, adding/removing elements)
  - Tuples (immutable collections)
  - Sets (unique collections)
  - Dictionaries (key-value pairs)
  - Range objects

### Day Five
- Object-Oriented Programming concepts
- Working with classes and objects

### SQL Integration
- Database connectivity
- Basic SQL operations
- CRUD operations with Python and SQL

## Files in this Repository

- [app.py](app.py): Introduction to Python basics with simple print statements
- [day_two.py](day_two.py): Comprehensive examples of variables, data types, and operators
- [day_three.py](day_three.py): Examples of control flow statements and functions
- [day_four.py](day_four.py): Examples of Python data structures
- [day_five.py](day_five.py): Introduction to Object-Oriented Programming
- [library_app.py](library_app.py): Implementation of the Library Management System challenge
- [config.py](config.py): Configuration file for database connections and environment variables
- [notes.txt](notes.txt): Outline of topics covered by day
- [LICENSE](LICENSE): MIT License for this project
- [.gitignore](.gitignore): Specifies intentionally untracked files to ignore (includes .env and env/)

## Library Management Application

The repository includes a complete Library Management System application that demonstrates:

### Components
- **Configuration** (`config.py`): Manages database connections and environment variables
- **Main Application** (`library_app.py`): Entry point for the library management system with the following features:
  - User authentication for librarians and members
  - Book catalog management
  - Borrowing and returning processes
  - Member management
  - Reporting functionality

### Database Structure
- Tables for Books, Members, Librarians, and Transactions
- Relationships between entities using foreign keys
- CRUD operations implemented for all main entities

### Running the Library Application
```bash
python library_app.py
```

## Challenges

The repository includes programming challenges to practice Python concepts:

- **Challenge One**: Building a library management system with classes for Person, Student, Book, and Librarian, demonstrating inheritance principles.

## Setting Up Virtual Environment

This project uses a virtual environment to manage dependencies. Follow these steps to set it up:

### On macOS/Linux:

1. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```

2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

### On Windows:

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

## Environment Variables

The project uses environment variables for sensitive information like database credentials. Create a `.env` file in the project root with the following variables:

```
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

These environment variables are loaded by `config.py` to establish database connections securely without exposing credentials in the code.

## Getting Started

To run these examples, you need Python installed on your system. You can run any of the Python files using:

```bash
python app.py
# or
python day_two.py
# or
python day_three.py
# or
python day_four.py
# or
python day_five.py
```

## Examples

The repository includes practical examples like:
- Basic printing and calculations
- Variable assignment and manipulation
- Rectangle calculator (user input, calculations, and output)
- Control flow demonstrations with loops and conditionals
- Function definitions with various parameter types
- Data structures implementation and manipulation
- Object-oriented programming implementations
- SQL database operations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.