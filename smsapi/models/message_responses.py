# -*- coding: utf-8 -*-

"""
    smsapi.models.message_responses

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class MessageResponses(object):

    """Implementation of the 'MessageResponses' model.

    TODO: type model description here.

    Attributes:
        mfrom (string): Phone number the response was sent from.
        acknowledged_timestamp (string): The date and time when the response
            was acknowledged.
        content (string): The response content.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom" : "from",
        "acknowledged_timestamp" : "acknowledgedTimestamp",
        "content" : "content"
    }

    def __init__(self,
                 mfrom=None,
                 acknowledged_timestamp=None,
                 content=None):
        """Constructor for the MessageResponses class"""

        # Initialize members of the class
        self.mfrom = mfrom
        self.acknowledged_timestamp = acknowledged_timestamp
        self.content = content


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mfrom = dictionary.get("from")
        acknowledged_timestamp = dictionary.get("acknowledgedTimestamp")
        content = dictionary.get("content")

        # Return an object of this model
        return cls(mfrom,
                   acknowledged_timestamp,
                   content)


