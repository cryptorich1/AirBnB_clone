#!/usr/bin/python3
""" Define the state clase. """
from models.base_model import BaseModel

clase State(BaseModel):
    """ Represent a state

    Attributes:
        name (str): The name of the state.
    """

    name = ""
