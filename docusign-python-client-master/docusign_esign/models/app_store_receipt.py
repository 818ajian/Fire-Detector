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


class AppStoreReceipt(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, receipt_data=None):
        """
        AppStoreReceipt - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'str',
            'receipt_data': 'str'
        }

        self.attribute_map = {
            'product_id': 'productId',
            'receipt_data': 'receiptData'
        }

        self._product_id = product_id
        self._receipt_data = receipt_data

    @property
    def product_id(self):
        """
        Gets the product_id of this AppStoreReceipt.
        

        :return: The product_id of this AppStoreReceipt.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this AppStoreReceipt.
        

        :param product_id: The product_id of this AppStoreReceipt.
        :type: str
        """

        self._product_id = product_id

    @property
    def receipt_data(self):
        """
        Gets the receipt_data of this AppStoreReceipt.
        Reserved: TBD

        :return: The receipt_data of this AppStoreReceipt.
        :rtype: str
        """
        return self._receipt_data

    @receipt_data.setter
    def receipt_data(self, receipt_data):
        """
        Sets the receipt_data of this AppStoreReceipt.
        Reserved: TBD

        :param receipt_data: The receipt_data of this AppStoreReceipt.
        :type: str
        """

        self._receipt_data = receipt_data

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
