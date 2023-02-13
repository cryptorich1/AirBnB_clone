#!/usr/bin/python3
"""
Define the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attribute:
    name (str): The name of the Amenity
    """
    name = ""
