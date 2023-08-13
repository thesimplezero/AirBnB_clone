#!/usr/bin/env python3
from models.base_model import BaseModel  # Import BaseModel class


class State(BaseModel):  # Inherit from BaseModel
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""  # Default value is an empty string
