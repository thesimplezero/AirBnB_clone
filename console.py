#!/usr/bin/env python3
import cmd
import shlex
from datetime import datetime
from models import storage

from models.base_model import BaseModel
from models.user import User
from models.city import City


classes = {"BaseModel": BaseModel, "User": User, "City": City}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit program"""
        return True

    def do_EOF(self, arg):
        """Exit program using Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
