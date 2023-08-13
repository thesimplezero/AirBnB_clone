#!/usr/bin/python3
"""
Unittests for the FileStorage class.
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        """Set up testing environment"""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Remove the testing file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all() method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Test the new() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objs = self.storage.all()
        self.assertIn("{}.{}".format(my_model.__class__.__name__, my_model.id), all_objs)

    def test_save(self):
        """Test the save() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            file_content = json.load(f)
        self.assertIn("{}.{}".format(my_model.__class__.__name__, my_model.id), file_content)

    def test_reload(self):
        """Test the reload() method"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("{}.{}".format(my_model.__class__.__name__, my_model.id), all_objs)

if __name__ == '__main__':
    unittest.main()
