# AIRBNB PROJECT

<p align="center">
  <img src="https://raw.githubusercontent.com/bdbaraban/AirBnB_clone/master/assets/hbnb_logo.png"/>
</p>

## Description of the project

This is the first part of the project that simulates an airbnb application in which we are creating a way to control the modules that our web page is going to use by intervening a database in json format. Here we apply object oriented programming, python data translation and command interpreted logic to deliver a local database that can be modified by commands.

<p align="center"> <img src="https://raw.githubusercontent.com/daorejuela1/AirBnB_clone/master/images/console_airbnb.png"/> </p>

## Installation

- Clone this repository: `git clone "https://github.com/JSM788/holbertonschool-AirBnB_clone.git"`

- Change directories into the repository: `cd holbertonschool-AirBnB_clone`

## Console
La consola es un intérprete de línea de comandos que permite la gestión del backend de HolbertonBnB. Se puede usar para manejar y manipular todas las clases utilizadas por la aplicación (logrado mediante llamadas al storageobjeto definido anteriormente).


## Run

- If you want to execute the console in interactive mode:
```
  ./console.py
```

- If you want to execute the console in non-interactive mode:
```
  echo "help" | ./console.py
```

## Available commands
|Command| Explanation |
|--|--|
| create | Create a new instance of a class, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`  |
| show | Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234` |
| all | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` |
| update | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` |




## Testing

- If you want to personalize the classes and execute unit tests to confirm that your changes haven't modify the functionality use:

```
  python3 -m unittest discover tests
```

- Alternatively, you can specify a single test file to run at a time:

```
  python3 unittest -m tests/test_console.py
```

<div>
 <video class="center" src="">⁪</video>
</div>

## Authors


- Juan Salinas | [GitHub](https://github.com/JSM788)
- Frank Christopher | [GitHub](https://github.com/QuispeFrank)
