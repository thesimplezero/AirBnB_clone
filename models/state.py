#!/usr/bin/env python3
from base_model import BaseModel
import os
import sys

# Get directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes new State instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
