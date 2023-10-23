# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class KnownAttribute(object):

    """Implementation of the 'known_attribute' model.

    TODO: type model description here.

    Attributes:
        attribute (str): TODO: type description here.
        value (str): TODO: type description here.
        name (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute": 'attribute',
        "value": 'value',
        "name": 'name'
    }

    def __init__(self,
                 attribute=None,
                 value=None,
                 name=None):
        """Constructor for the KnownAttribute class"""

        # Initialize members of the class
        self.attribute = attribute 
        self.value = value 
        self.name = name 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        attribute = dictionary.get("attribute") if dictionary.get("attribute") else None
        value = dictionary.get("value") if dictionary.get("value") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        # Return an object of this model
        return cls(attribute,
                   value,
                   name)
