# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Instruction5(object):

    """Implementation of the 'Instruction5' model.

    TODO: type model description here.

    Attributes:
        evaluate (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "evaluate": 'evaluate'
    }

    def __init__(self,
                 evaluate=None):
        """Constructor for the Instruction5 class"""

        # Initialize members of the class
        self.evaluate = evaluate 

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
        evaluate = dictionary.get("evaluate") if dictionary.get("evaluate") else None
        # Return an object of this model
        return cls(evaluate)