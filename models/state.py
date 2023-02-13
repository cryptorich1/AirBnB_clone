#!/usr/bin/python3
""" Define the state clase. """
from models.base_model import BaseModel

class State(BaseModel):
    """ Represent a state

    Attributes:
        name (str): The name of the state.
    """

    name = ""
