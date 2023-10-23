# -*- coding: utf-8 -*-

"""
scrapingbee

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.query_auth import QueryAuth


class CustomQueryAuthentication(QueryAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in CustomQueryAuthentication

        """
        return "CustomQueryAuthentication: api_key is undefined."

    def __init__(self, api_key):
        auth_params = {}
        if api_key:
            auth_params["api_key"] = api_key
        super().__init__(auth_params=auth_params)
        self._api_key = api_key