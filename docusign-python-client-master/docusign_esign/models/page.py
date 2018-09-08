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


class Page(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dpi=None, error_details=None, height=None, image_bytes=None, mime_type=None, page_id=None, sequence=None, width=None):
        """
        Page - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dpi': 'str',
            'error_details': 'ErrorDetails',
            'height': 'str',
            'image_bytes': 'str',
            'mime_type': 'str',
            'page_id': 'str',
            'sequence': 'str',
            'width': 'str'
        }

        self.attribute_map = {
            'dpi': 'dpi',
            'error_details': 'errorDetails',
            'height': 'height',
            'image_bytes': 'imageBytes',
            'mime_type': 'mimeType',
            'page_id': 'pageId',
            'sequence': 'sequence',
            'width': 'width'
        }

        self._dpi = dpi
        self._error_details = error_details
        self._height = height
        self._image_bytes = image_bytes
        self._mime_type = mime_type
        self._page_id = page_id
        self._sequence = sequence
        self._width = width

    @property
    def dpi(self):
        """
        Gets the dpi of this Page.
        The number of dots per inch used for the page image.

        :return: The dpi of this Page.
        :rtype: str
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """
        Sets the dpi of this Page.
        The number of dots per inch used for the page image.

        :param dpi: The dpi of this Page.
        :type: str
        """

        self._dpi = dpi

    @property
    def error_details(self):
        """
        Gets the error_details of this Page.

        :return: The error_details of this Page.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this Page.

        :param error_details: The error_details of this Page.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def height(self):
        """
        Gets the height of this Page.
        Height of the tab in pixels.

        :return: The height of this Page.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Page.
        Height of the tab in pixels.

        :param height: The height of this Page.
        :type: str
        """

        self._height = height

    @property
    def image_bytes(self):
        """
        Gets the image_bytes of this Page.
        

        :return: The image_bytes of this Page.
        :rtype: str
        """
        return self._image_bytes

    @image_bytes.setter
    def image_bytes(self, image_bytes):
        """
        Sets the image_bytes of this Page.
        

        :param image_bytes: The image_bytes of this Page.
        :type: str
        """

        self._image_bytes = image_bytes

    @property
    def mime_type(self):
        """
        Gets the mime_type of this Page.
        

        :return: The mime_type of this Page.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this Page.
        

        :param mime_type: The mime_type of this Page.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def page_id(self):
        """
        Gets the page_id of this Page.
        

        :return: The page_id of this Page.
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """
        Sets the page_id of this Page.
        

        :param page_id: The page_id of this Page.
        :type: str
        """

        self._page_id = page_id

    @property
    def sequence(self):
        """
        Gets the sequence of this Page.
        

        :return: The sequence of this Page.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this Page.
        

        :param sequence: The sequence of this Page.
        :type: str
        """

        self._sequence = sequence

    @property
    def width(self):
        """
        Gets the width of this Page.
        Width of the tab in pixels.

        :return: The width of this Page.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Page.
        Width of the tab in pixels.

        :param width: The width of this Page.
        :type: str
        """

        self._width = width

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
