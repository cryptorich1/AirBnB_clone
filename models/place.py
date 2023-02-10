#!/usr/bin/python3
""""Define the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attribute:
    city_id (str): The City id.
    user_id (str): The User is.
    name (str): The name of the place.
    description (str): The description of the place.
    number_rooms (int): The number of the rooms of the house
    number_bathrooms (int): The number of the bathrooms of the house.
    max_guest (int): The maximuim number of guests in the room
    price_per_night (int): the price per night for the room.
    latitude (float): The latitude of the place.
    longitude (float): The longitude of the place
    amenity_id (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
