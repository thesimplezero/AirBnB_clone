#!/usr/bin/env python3
from models.base_model import BaseModel  # Import BaseModel class


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""  # Initialize with empty string

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
