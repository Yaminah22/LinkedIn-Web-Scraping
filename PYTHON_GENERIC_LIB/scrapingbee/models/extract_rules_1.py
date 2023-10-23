# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from scrapingbee.models.all_links import AllLinks


class ExtractRules1(object):

    """Implementation of the 'extract_rules1' model.

    TODO: type model description here.

    Attributes:
        all_links (AllLinks): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "all_links": 'all_links'
    }

    def __init__(self,
                 all_links=None):
        """Constructor for the ExtractRules1 class"""

        # Initialize members of the class
        self.all_links = all_links 

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
        all_links = AllLinks.from_dictionary(dictionary.get('all_links')) if dictionary.get('all_links') else None
        # Return an object of this model
        return cls(all_links)