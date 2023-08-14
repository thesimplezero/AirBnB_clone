#!/usr/bin/python3
"""
This module defines the FileStorage class that serializes instances
to a JSON file and deserializes JSON files to instances.
"""
import json
import os
from base_model import BaseModel
import os
import sys

# Get directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


class FileStorage:
    """
    This class manages the serialization and deserialization of instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
