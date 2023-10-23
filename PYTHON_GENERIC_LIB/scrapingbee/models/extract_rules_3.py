# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from scrapingbee.models.email_addresses import EmailAddresses


class ExtractRules3(object):

    """Implementation of the 'extract_rules3' model.

    TODO: type model description here.

    Attributes:
        email_addresses (EmailAddresses): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email_addresses": 'email_addresses'
    }

    def __init__(self,
                 email_addresses=None):
        """Constructor for the ExtractRules3 class"""

        # Initialize members of the class
        self.email_addresses = email_addresses 

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
        email_addresses = EmailAddresses.from_dictionary(dictionary.get('email_addresses')) if dictionary.get('email_addresses') else None
        # Return an object of this model
        return cls(email_addresses)