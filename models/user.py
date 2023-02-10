#!/usr/bin/python3
""" Define the User class. """
from models.base_model import BaseModel


clase User(BaseModel):
    """ Represent a user 

    Attributes:
        first_name (str): The user first name.
        last_name (str): The last name of the user.
        email (str): The user email.
        password (str): The user password
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
