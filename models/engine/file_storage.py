#!/usr/bin/python3
""" Define the engine class. """
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State


class FIleStorage:
    """ Serialize an instance to JSON and deserializes
    back to instance object """

    # store all object by class <class name>.id
    __objects = {}
    # path to the JSON file.
    __file__path = "file.json"

    def all(self, cls=None):
        """ Returns a dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """ Sets in __objects, the obj with key <obj class name>.id"""
        if obj is not None:
            # Concatenate class object name with id.
            key = obj.__class__.__name__ + "." + obj.id
            # update the __object dictionary with the new key and object as value
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file(path:__file__path)"""
        j_objects = {}
        # for the python data to be serialized, the data stored inside the __object
        # variable as objects must be converted to a dictionary so that python
        # for json to understand using to_dict method of the basemodel class
        # The result of this will be a key with a unique dictionary as the value
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
            # convert the dictionary into json and save in __filepath.
            with open(self.__file__path, 'w') as f:
                json.dump(j_objects, f)

        def reload(self):
        """
        Deserializes the JSON file to __objs(only is the JSON file(__file_path)
        exists; otherwise do nothing, no exception should be raised
        if the file does not exist.
        """

        try:
            with open(self.__file__path, 'r', encoding="utf8") as f:
                # The load method deserializes a json string into a python dict.
                obj_dict = json.load(f)
            for obj_item in obj_dict.values():
                # Extract the class from which to instantiate an object.
                # Remember we loaded the values not the key
                class_name = obj_item["__class__"]
                # Since we are creating object instances, the attribute __class__\
                # Should not be as part of the arguments to the init
                # function of the class(identified by class_name) all the other
                # arguments are valid.
                del obj_item["__class__"]
                # use the previously defined new function to create a new __obj.
                # The double asterics expands the dictionary to allow every key.
                # value pair from the object_item dictionary to be passed to the __init__()
                # method of the class identified by class_name
                self.new(eval(class_name)(**obj_item))
        except:
            pass
