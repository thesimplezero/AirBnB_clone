#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
import os
import sys

# Get directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
