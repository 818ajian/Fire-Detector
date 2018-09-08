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


class TemplateRecipients(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, agents=None, carbon_copies=None, certified_deliveries=None, current_routing_order=None, editors=None, error_details=None, in_person_signers=None, intermediaries=None, recipient_count=None, signers=None):
        """
        TemplateRecipients - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agents': 'list[Agent]',
            'carbon_copies': 'list[CarbonCopy]',
            'certified_deliveries': 'list[CertifiedDelivery]',
            'current_routing_order': 'str',
            'editors': 'list[Editor]',
            'error_details': 'ErrorDetails',
            'in_person_signers': 'list[InPersonSigner]',
            'intermediaries': 'list[Intermediary]',
            'recipient_count': 'str',
            'signers': 'list[Signer]'
        }

        self.attribute_map = {
            'agents': 'agents',
            'carbon_copies': 'carbonCopies',
            'certified_deliveries': 'certifiedDeliveries',
            'current_routing_order': 'currentRoutingOrder',
            'editors': 'editors',
            'error_details': 'errorDetails',
            'in_person_signers': 'inPersonSigners',
            'intermediaries': 'intermediaries',
            'recipient_count': 'recipientCount',
            'signers': 'signers'
        }

        self._agents = agents
        self._carbon_copies = carbon_copies
        self._certified_deliveries = certified_deliveries
        self._current_routing_order = current_routing_order
        self._editors = editors
        self._error_details = error_details
        self._in_person_signers = in_person_signers
        self._intermediaries = intermediaries
        self._recipient_count = recipient_count
        self._signers = signers

    @property
    def agents(self):
        """
        Gets the agents of this TemplateRecipients.
        A complex type defining the management and access rights of a recipient assigned assigned as an agent on the document.

        :return: The agents of this TemplateRecipients.
        :rtype: list[Agent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """
        Sets the agents of this TemplateRecipients.
        A complex type defining the management and access rights of a recipient assigned assigned as an agent on the document.

        :param agents: The agents of this TemplateRecipients.
        :type: list[Agent]
        """

        self._agents = agents

    @property
    def carbon_copies(self):
        """
        Gets the carbon_copies of this TemplateRecipients.
        A complex type containing information about recipients who should receive a copy of the envelope, but does not need to sign it.

        :return: The carbon_copies of this TemplateRecipients.
        :rtype: list[CarbonCopy]
        """
        return self._carbon_copies

    @carbon_copies.setter
    def carbon_copies(self, carbon_copies):
        """
        Sets the carbon_copies of this TemplateRecipients.
        A complex type containing information about recipients who should receive a copy of the envelope, but does not need to sign it.

        :param carbon_copies: The carbon_copies of this TemplateRecipients.
        :type: list[CarbonCopy]
        """

        self._carbon_copies = carbon_copies

    @property
    def certified_deliveries(self):
        """
        Gets the certified_deliveries of this TemplateRecipients.
        A complex type containing information on a recipient the must receive the completed documents for the envelope to be completed, but the recipient does not need to sign, initial, date, or add information to any of the documents.

        :return: The certified_deliveries of this TemplateRecipients.
        :rtype: list[CertifiedDelivery]
        """
        return self._certified_deliveries

    @certified_deliveries.setter
    def certified_deliveries(self, certified_deliveries):
        """
        Sets the certified_deliveries of this TemplateRecipients.
        A complex type containing information on a recipient the must receive the completed documents for the envelope to be completed, but the recipient does not need to sign, initial, date, or add information to any of the documents.

        :param certified_deliveries: The certified_deliveries of this TemplateRecipients.
        :type: list[CertifiedDelivery]
        """

        self._certified_deliveries = certified_deliveries

    @property
    def current_routing_order(self):
        """
        Gets the current_routing_order of this TemplateRecipients.
        

        :return: The current_routing_order of this TemplateRecipients.
        :rtype: str
        """
        return self._current_routing_order

    @current_routing_order.setter
    def current_routing_order(self, current_routing_order):
        """
        Sets the current_routing_order of this TemplateRecipients.
        

        :param current_routing_order: The current_routing_order of this TemplateRecipients.
        :type: str
        """

        self._current_routing_order = current_routing_order

    @property
    def editors(self):
        """
        Gets the editors of this TemplateRecipients.
        

        :return: The editors of this TemplateRecipients.
        :rtype: list[Editor]
        """
        return self._editors

    @editors.setter
    def editors(self, editors):
        """
        Sets the editors of this TemplateRecipients.
        

        :param editors: The editors of this TemplateRecipients.
        :type: list[Editor]
        """

        self._editors = editors

    @property
    def error_details(self):
        """
        Gets the error_details of this TemplateRecipients.

        :return: The error_details of this TemplateRecipients.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this TemplateRecipients.

        :param error_details: The error_details of this TemplateRecipients.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def in_person_signers(self):
        """
        Gets the in_person_signers of this TemplateRecipients.
        Specifies a signer that is in the same physical location as a DocuSign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.

        :return: The in_person_signers of this TemplateRecipients.
        :rtype: list[InPersonSigner]
        """
        return self._in_person_signers

    @in_person_signers.setter
    def in_person_signers(self, in_person_signers):
        """
        Sets the in_person_signers of this TemplateRecipients.
        Specifies a signer that is in the same physical location as a DocuSign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.

        :param in_person_signers: The in_person_signers of this TemplateRecipients.
        :type: list[InPersonSigner]
        """

        self._in_person_signers = in_person_signers

    @property
    def intermediaries(self):
        """
        Gets the intermediaries of this TemplateRecipients.
        Identifies a recipient that can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).

        :return: The intermediaries of this TemplateRecipients.
        :rtype: list[Intermediary]
        """
        return self._intermediaries

    @intermediaries.setter
    def intermediaries(self, intermediaries):
        """
        Sets the intermediaries of this TemplateRecipients.
        Identifies a recipient that can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).

        :param intermediaries: The intermediaries of this TemplateRecipients.
        :type: list[Intermediary]
        """

        self._intermediaries = intermediaries

    @property
    def recipient_count(self):
        """
        Gets the recipient_count of this TemplateRecipients.
        The list of recipient event statuses that will trigger Connect to send updates to the url. It can be a two-part list with:  * recipientEventStatusCode - The recipient status, this can be Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded. * includeDocuments - When set to **true**, the envelope time zone information is included in the message.

        :return: The recipient_count of this TemplateRecipients.
        :rtype: str
        """
        return self._recipient_count

    @recipient_count.setter
    def recipient_count(self, recipient_count):
        """
        Sets the recipient_count of this TemplateRecipients.
        The list of recipient event statuses that will trigger Connect to send updates to the url. It can be a two-part list with:  * recipientEventStatusCode - The recipient status, this can be Sent, Delivered, Completed, Declined, AuthenticationFailed, and AutoResponded. * includeDocuments - When set to **true**, the envelope time zone information is included in the message.

        :param recipient_count: The recipient_count of this TemplateRecipients.
        :type: str
        """

        self._recipient_count = recipient_count

    @property
    def signers(self):
        """
        Gets the signers of this TemplateRecipients.
        A complex type containing information about the Signer recipient.

        :return: The signers of this TemplateRecipients.
        :rtype: list[Signer]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """
        Sets the signers of this TemplateRecipients.
        A complex type containing information about the Signer recipient.

        :param signers: The signers of this TemplateRecipients.
        :type: list[Signer]
        """

        self._signers = signers

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
