# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExternalDocServiceErrorDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, authentication_url=None, error_code=None, message=None):
        """
        ExternalDocServiceErrorDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authentication_url': 'str',
            'error_code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'authentication_url': 'authenticationUrl',
            'error_code': 'errorCode',
            'message': 'message'
        }

        self._authentication_url = authentication_url
        self._error_code = error_code
        self._message = message

    @property
    def authentication_url(self):
        """
        Gets the authentication_url of this ExternalDocServiceErrorDetails.
        Reserved: TBD

        :return: The authentication_url of this ExternalDocServiceErrorDetails.
        :rtype: str
        """
        return self._authentication_url

    @authentication_url.setter
    def authentication_url(self, authentication_url):
        """
        Sets the authentication_url of this ExternalDocServiceErrorDetails.
        Reserved: TBD

        :param authentication_url: The authentication_url of this ExternalDocServiceErrorDetails.
        :type: str
        """

        self._authentication_url = authentication_url

    @property
    def error_code(self):
        """
        Gets the error_code of this ExternalDocServiceErrorDetails.
        

        :return: The error_code of this ExternalDocServiceErrorDetails.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this ExternalDocServiceErrorDetails.
        

        :param error_code: The error_code of this ExternalDocServiceErrorDetails.
        :type: str
        """

        self._error_code = error_code

    @property
    def message(self):
        """
        Gets the message of this ExternalDocServiceErrorDetails.
        

        :return: The message of this ExternalDocServiceErrorDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ExternalDocServiceErrorDetails.
        

        :param message: The message of this ExternalDocServiceErrorDetails.
        :type: str
        """

        self._message = message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
