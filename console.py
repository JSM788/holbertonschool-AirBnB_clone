#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "


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
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            o = BaseModel()
            o.save()
            print(o.id)

    def do_show(self, arg):
        all_dict = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in all_dict:
            print("** no instance found **")
        else:
            print(all_dict[f"{arg[0]}{arg[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        json_to_dic = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) != 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in json_to_dic:
            print('** no instance found **')
        else:
            del json_to_dic[f'{args[0]}.{args[1]}']
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
