#!/usr/bin/env python3
from base_model import BaseModel


class Place(BaseModel):
    """
    A class representing rental property.
    Inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes for a Place instance.
        Attributes:
        - city_id (str): ID of the associated city (default: "").
        - user_id (str): ID of the user who owns the place (default: "").
        - name (str): Name of the place (default: "").
        - description (str): Description of the place (default: "").
        - number_rooms (int): Number of rooms (default: 0).
        - number_bathrooms (int): Number of bathrooms (default: 0).
        - max_guest (int): Maximum number of guests (default: 0).
        - price_by_night (int): Price per night (default: 0).
        - latitude (float): Latitude coordinate (default: 0.0).
        - longitude (float): Longitude coordinate (default: 0.0).
        - amenity_ids (list): List of amenity IDs (default: []).
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
