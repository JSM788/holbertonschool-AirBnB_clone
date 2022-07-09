
<h1 align="center">AIRBNB PROJECT</h1>


<p align="center">
  <img src="https://github.com/JSM788/holbertonschool-AirBnB_clone/blob/main/visual/HBNB%20holberton.png"/>
</p>

## Description of the project

This is the first part of the project that simulates an airbnb application in which we are creating a way to control the modules that our web page is going to use by intervening a database in json format. Here we apply object oriented programming, python data translation and command interpreted logic to deliver a local database that can be modified by commands.

<p align="center"> <img src="https://github.com/JSM788/holbertonschool-AirBnB_clone/blob/main/visual/Consola.png"/> </p>

## Installation

- Clone this repository: `git clone "https://github.com/JSM788/holbertonschool-AirBnB_clone.git"`

- Change directories into the repository: `cd holbertonschool-AirBnB_clone`

## Console
The console is a command line interpreter that allows the management of the AIRBNB backend. It can be used to handle and manipulate all the classes used by the application (achieved by calls to the storage object defined above).


## Run

- If you want to execute the console in interactive mode:
```
$ ./console.py
(hbnb) help


Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
```

- If you want to execute the console in non-interactive mode:
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
```

## Available commands
|Command| Explanation |
|--|--|
| create | Create a new instance of a class, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`  |
| show | Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234` |
| all | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` |
| update | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` |


<p align="center">
  <img src="https://github.com/JSM788/holbertonschool-AirBnB_clone/blob/main/visual/commands.gif"/>
</p>

## Command usage examples

The HolbertonBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

```
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2022-07-03T2
1:30:42.215277", "created_at": "2022-07-03T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
```

* **show**
  * Usage: `show <class> <id>`

```
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2022, 7, 3, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2022, 7, 3, 21, 34, 3, 635828)}
(hbnb) 
```

* **destroy**
  * Usage: `destroy <class> <id>`

```
$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) create Place
03486a3e-8329-4f47-9947-dca80c03d3ed
(hbnb)
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) destroy Place 03486a3e-8329-4f47-9947-dca80c03d3ed
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>`

```
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2022, 7, 3, 21, 45, 5, 963516), 'created_at': datetime.datetime(2022, 7
, 3, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2022, 7, 3, 21, 43, 56, 899348), 'created_at': datetime.datetime(2022, 7, 3,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) all User
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2022, 7, 3, 21, 44, 44, 428413), 'created_at': datetime.datetime(2022, 7, 3
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
(b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2022, 7
, 3, 21, 44, 15, 974608), 'created_at': datetime.datetime(2022, 7, 3, 21, 44,
15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb) 
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetim
e(2022, 7, 3, 21, 44, 44, 428413), 'created_at': datetime.datetime(2022, 7, 3
, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
del] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(20
22, 7, 3, 21, 45, 5, 963516), 'created_at': datetime.datetime(2022, 7, 3, 21,
45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2022, 7, 3, 2
1, 44, 15, 974608), 'created_at': datetime.datetime(2022, 7, 3, 21, 44, 15, 97
4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2022, 7, 3, 21, 4
3, 56, 899348), 'created_at': datetime.datetime(2022, 7, 3, 21, 43, 56, 899348
), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb) 
```


* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"`
```
$ ./console.py
(hbnb) create User
 6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2022, 7, 3, 21, 54, 39, 234382), 'updated_at': datetime.datetime(2022, 7, 3, 21
, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-ef0fdc863c02'}
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2022, 7, 3, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2022, 7, 3, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
(hbnb)
```

## Testing

- If you want to personalize the classes and execute unit tests to confirm that your changes haven't modify the functionality use:

```
  python3 -m unittest discover tests
```

- Alternatively, you can specify a single test file to run at a time:

```
  python3 unittest -m tests/test_console.py
```


## Authors


- Juan Salinas | [GitHub](https://github.com/JSM788)
- Frank Quispe | [GitHub](https://github.com/QuispeFrank)
