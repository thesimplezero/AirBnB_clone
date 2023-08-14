#!/usr/bin/python3
"""Unit tests for user class"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class Test_User(unittest.TestCase):
    """Test casess for User class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.user = User()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        del self.user

    def test_init_with_arguments(self):
        """Test initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.user = User(**data)

        # Verify that the attributes are set correctly
        self.assertEqual(self.user.id, '123')
        self.assertEqual(self.user.created_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.user.updated_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.user.name, 'Test')

    def test_instance_creation(self):
        """tests if an instance is created the right way"""
        self.assertIsInstance(self.user, User)

    def test_init_without_arguments(self):
        """Test initialization without arguments"""
        self.user = User()

        # Verify that the attributes are set correctly
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_args(self):
        """Testing args which was unused"""
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_with_kwargs(self):
        """Testing with kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        usr = User(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(usr.id, "123")
        self.assertEqual(usr.created_at, date)
        self.assertEqual(usr.updated_at, date)

    def test_kwargs_None(self):
        """Testing with kwargs at None"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        """ testing with both args and kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        usr = User(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(usr.id, "123")
        self.assertEqual(usr.created_at, date)
        self.assertEqual(usr.updated_at, date)

    def test_attributes(self):
        """tests the attributes for class user"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))


if __name__ == "__main__":
    unittest.main()
