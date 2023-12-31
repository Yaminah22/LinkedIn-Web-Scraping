# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RelatedSearches(object):

    """Implementation of the 'related_searches' model.

    TODO: type model description here.

    Attributes:
        query (str): TODO: type description here.
        link (str): TODO: type description here.
        mtype (str): TODO: type description here.
        position (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "query": 'query',
        "link": 'link',
        "mtype": 'type',
        "position": 'position'
    }

    def __init__(self,
                 query=None,
                 link=None,
                 mtype=None,
                 position=None):
        """Constructor for the RelatedSearches class"""

        # Initialize members of the class
        self.query = query 
        self.link = link 
        self.mtype = mtype 
        self.position = position 

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
        query = dictionary.get("query") if dictionary.get("query") else None
        link = dictionary.get("link") if dictionary.get("link") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        position = dictionary.get("position") if dictionary.get("position") else None
        # Return an object of this model
        return cls(query,
                   link,
                   mtype,
                   position)
