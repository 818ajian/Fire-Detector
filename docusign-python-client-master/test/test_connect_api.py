# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import docusign_esign
from docusign_esign.rest import ApiException
from docusign_esign.apis.connect_api import ConnectApi


class TestConnectApi(unittest.TestCase):
    """ ConnectApi unit test stubs """

    def setUp(self):
        self.api = docusign_esign.apis.connect_api.ConnectApi()

    def tearDown(self):
        pass

    def test_create_configuration(self):
        """
        Test case for create_configuration

        Creates a connect configuration for the specified account.
        """
        pass

    def test_delete_configuration(self):
        """
        Test case for delete_configuration

        Deletes the specified connect configuration.
        """
        pass

    def test_delete_event_failure_log(self):
        """
        Test case for delete_event_failure_log

        Deletes a Connect failure log entry.
        """
        pass

    def test_delete_event_log(self):
        """
        Test case for delete_event_log

        Deletes a specified Connect log entry.
        """
        pass

    def test_delete_event_logs(self):
        """
        Test case for delete_event_logs

        Gets a list of Connect log entries.
        """
        pass

    def test_delete_mobile_notifiers(self):
        """
        Test case for delete_mobile_notifiers

        Reserved
        """
        pass

    def test_get_configuration(self):
        """
        Test case for get_configuration

        Get a Connect Configuration Information
        """
        pass

    def test_get_event_log(self):
        """
        Test case for get_event_log

        Get the specified Connect log entry.
        """
        pass

    def test_list_configurations(self):
        """
        Test case for list_configurations

        Get Connect Configuration Information
        """
        pass

    def test_list_event_failure_logs(self):
        """
        Test case for list_event_failure_logs

        Gets the Connect failure log information.
        """
        pass

    def test_list_event_logs(self):
        """
        Test case for list_event_logs

        Gets the Connect log.
        """
        pass

    def test_list_mobile_notifiers(self):
        """
        Test case for list_mobile_notifiers

        Reserved
        """
        pass

    def test_list_users(self):
        """
        Test case for list_users

        Returns users from the configured Connect service.
        """
        pass

    def test_retry_event_for_envelope(self):
        """
        Test case for retry_event_for_envelope

        Republishes Connect information for the specified envelope.
        """
        pass

    def test_retry_event_for_envelopes(self):
        """
        Test case for retry_event_for_envelopes

        Republishes Connect information for multiple envelopes.
        """
        pass

    def test_update_configuration(self):
        """
        Test case for update_configuration

        Updates a specified Connect configuration.
        """
        pass

    def test_update_mobile_notifiers(self):
        """
        Test case for update_mobile_notifiers

        Reserved
        """
        pass


if __name__ == '__main__':
    unittest.main()
