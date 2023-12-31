# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Instruction2(object):

    """Implementation of the 'Instruction2' model.

    TODO: type model description here.

    Attributes:
        scroll_x (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scroll_x": 'scroll_x'
    }

    def __init__(self,
                 scroll_x=None):
        """Constructor for the Instruction2 class"""

        # Initialize members of the class
        self.scroll_x = scroll_x 

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
        scroll_x = dictionary.get("scroll_x") if dictionary.get("scroll_x") else None
        # Return an object of this model
        return cls(scroll_x)
