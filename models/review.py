#!/usr/bin/env python3
from base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review for a place.
    Inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes for a Review instance.
        Attributes:
        - place_id (str): ID of the associated place (default: "").
        - user_id (str): ID of user who wrote the review (default: "").
        - text (str): Text content of the review (default: "").
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
