#!/usr/bin/python3
import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
