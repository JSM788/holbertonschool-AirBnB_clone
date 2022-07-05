#!/usr/bin/python3
""" Defines the HBnB console """
import cmd
import re
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


def tf(x):
    """
    Evaluates the expression passed to this method
    """
    try:
        return(eval(x))
    except (NameError, SyntaxError):
        return(x)


class HBNBCommand(cmd.Cmd):
    """
    Defining the HBNBCommand command
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program\n"""
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            o = HBNBCommand.classes[args[0]]()
            o.save()
            print(o.id)
        """

        """

    def do_show(self, arg):
        """
        Display the string representation\
        of a class instance of a given id
        """
        all_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in all_dict:
            print("** no instance found **")
        else:
            print(all_dict[f"{args[0]}.{args[1]}"])
        """

        """

    def do_destroy(self, arg):
        """
        Delete a class instance of a given id
        """
        args = arg.split()
        json_to_dic = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) != 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in json_to_dic:
            print('** no instance found **')
        else:
            del json_to_dic[f'{args[0]}.{args[1]}']
            storage.save()
        """

        """

    def do_update(self, arg):
        """
        Update a class instance\
        of a given id by adding or updating\
        a given attribute key/value pair or dictionary
        """
        args = arg.split()
        json_to_dic = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in json_to_dic:
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            o = json_to_dic[f'{args[0]}.{args[1]}']
            setattr(o, args[2], tf(args[3]))
            o.save()
        """

        """

    def do_all(self, arg):
        """
        Display string representations\
        of all instances of a given class
        """
        args = arg.split()
        lst = []
        if len(args) > 0 and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif args:
            for i in storage.all().values():
                if args[0] == i.__class__.__name__:
                    lst.append(str(i))
        else:
            for i in storage.all().values():
                lst.append(str(i))

        if len(lst):
            print(lst)
        """

        """

    def default(self, arg):
        """default method.

        Args:
            arg: User input.
        """
        try:
            classname = re.findall(".*\\.", arg)[0][:-1]
            methodname = re.findall("\\..*\\(", arg)[0][1:-1]
            arguments = eval(re.findall("\\(.*\\)", arg)[0])
        except BaseException:
            print("Invalid Input - retry...")
            return

        methods = {
            "show": self.do_show,  # 2 arguments classname id
            "all": self.do_all,  # 1 argument classname
            "destroy": self.do_destroy,  # 2 arguments classname id
            "update": self.do_update,  # 4 arguments classname id attr value
            "count": self.do_count  # 1 argument classname
        }

        if methodname not in methods:
            return

        if isinstance(arguments, str):
            args = arguments
        elif len(arguments) >= 2 and isinstance(arguments[1], dict):
            dictionary = arguments[1]
            for k, v in dictionary.items():
                args = f'{arguments[0]} {k} {v}'
                methods[methodname](f'{classname} {args}')
            return
        else:
            try:
                args = ' '.join(arguments)
            except BaseException:
                args = ''
        methods[methodname](f'{classname} {args}')
        """

        """

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class
        """
        args = arg.split()
        if args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't  exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)
        """

        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
