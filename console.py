#!/usr/bin/env python3
import os
import sys

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import cmd
import models
from datetime import datetime
from shlex import shlex

from models.engine import storage
from base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User



classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

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

    def do_create(self, clsname=None):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not clsname:
            print('** class name missing **')
        elif not self.clslist.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[clsname]()
            storage.new(obj)  # Save the new instance
            storage.save()     # Save changes to storage
            print(obj.id)

    def do_all(self, arg):
        """Prints all instances based or not on the class name"""
        if arg and arg not in self.clslist:
            print("** class doesn't exist **")
            return
        instances = storage.all()

        if not arg:
            print([str(v) for v in instances.values()])
        else:
            print([str(v) for k, v in instances.items() if k.startswith(arg)])

    def do_show(self, arg):
        """Show instance based on id"""
        classname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not classname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.classes.get(classname):
            print("** class doesn't exist **")
        else:
            k = classname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """destroy instance based on id
        """
        classname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not classname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.classes.get(classname):
            print("** class doesn't exist **")
        else:
            k = classname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
