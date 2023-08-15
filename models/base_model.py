#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as
the base class for other classes.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class defines the common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing the base model
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

