# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ExtractRules(object):

    """Implementation of the 'extract_rules' model.

    TODO: type model description here.

    Attributes:
        title (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title'
    }

    def __init__(self,
                 title=None):
        """Constructor for the ExtractRules class"""

        # Initialize members of the class
        self.title = title 

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
        title = dictionary.get("title") if dictionary.get("title") else None
        # Return an object of this model
        return cls(title)