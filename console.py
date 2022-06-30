#!/usr/bin/python3
import cmd

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
