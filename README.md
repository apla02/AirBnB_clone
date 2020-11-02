# 0x00. AirBnB clone - The console

## 🚀 Description of the project

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…  

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

- create the first abstracted storage engine of the project: File storage.

- create all unittests to validate all our classes and storage engine

## 📑 Learning Objectives
- How to create a Python package
- How to create a command 
- interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## ✔️ General Requirements
### ▶️ Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### ▶️ Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## ⚙ Instalation
```
git clone https://github.com/apla02/AirBnB_clone
```

## 💻 Usage
### It should works like this in interactive mode:  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### It should works like this in non-interactive mode:  
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
##  ⌨️ Description of the commands  

| Command      | Description |
| :---        |    :----:   |
| help | Shows documentation of the commands.       |
| EOF  | To exit the program        |
| quit |To exit the program        |
| create | Creates a new instance       |
| show  | Prints the string rep of an instance        |
| destroy | Deletes an instance        |  
| all | Prints all the string rep of all instances        | 
| update | Updates an instance        |  
  

#### Usage:  

Let's suposed the id number is 121212, the class name is BaseModel, first_name is the attribute name and Betty is the attribute value

```
(hbnb) help
(hbnb) help quit
(hbnb) create BaseModel 
(hbnb) show BaseModel 121212
(hbnb) destroy BaseModel 121212
(hbnb) all BaseModel
(hbnb) all BaseModel 121212 first_name "Betty"

```

#### Example:   

```
~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
~/AirBnB$
```  


## 📂 Repository Contents  
Simple Shell files:
File  | Description
------------- | -------------
[models](https://github.com/apla02/AirBnB_clone/tree/main/models "models")  | Contains BaseModel class and the others.
[models/__init__.py](https://github.com/apla02/AirBnB_clone/tree/main/models/__init__.py "__init__")  | __init__ file.
[models/amenity.py](https://github.com/apla02/AirBnB_clone/tree/main/models/amenity.py "amenity.py")  | Contains the Amenity class.
[models/base_model.py](https://github.com/apla02/AirBnB_clone/tree/main/models/base_model.py "base_model.py")  | Contains the BaseModel class.
[models/city.py](https://github.com/apla02/AirBnB_clone/tree/main/models/base_model.py "city.py")  | Contains the City class.
[models/place.py](https://github.com/apla02/AirBnB_clone/tree/main/models/place.py "place.py")  | Contains the Place class.
[models/review.py](https://github.com/apla02/AirBnB_clone/tree/main/models/review.py "review.py")  | Contains the Review class.
[models/state.py](https://github.com/apla02/AirBnB_clone/tree/main/models/state.py "state.py")  | Contains the State class.
[models/user.py](https://github.com/apla02/AirBnB_clone/tree/main/models/user.py "user.py")  | Contains the User class.
[models/engine/file_storage.py](https://github.com/apla02/AirBnB_clone/blob/main/models/engine/file_storage.py "file_storage.py")  | Contains the FileStorage class.
[models/engine/__init__.py](https://github.com/apla02/AirBnB_clone/blob/main/models/engine/__init__.py "__init__.py")  | __init__ file.
[tests](https://github.com/Valentinaga1/simple_shell/blob/master/tests "tests")  |  Contains tests cases.
[tests/test_models](https://github.com/Valentinaga1/simple_shell/blob/master/tests/test_models "tes/test_modelsts")  |  Contains tests cases.
[AUTHORS](https://github.com/Valentinaga1/simple_shell/blob/master/AUTHORS "AUTHORS")  | Contains the Authors names of the project.
[console.py](https://github.com/Valentinaga1/simple_shell/blob/master/console.py "console.py")  | Contains the console class.  }

## 🚀Authors
* **Laura Andrea Álvarez Pérez** - *Holberton School Student* - [apla02](https://github.com/apla02)
* **Valentina Gómez Agudelo** - *Holberton School Student* - [Valentinaga1](https://github.com/Valentinaga1)

