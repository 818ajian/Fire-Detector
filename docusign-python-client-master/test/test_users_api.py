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
from docusign_esign.apis.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """ UsersApi unit test stubs """

    def setUp(self):
        self.api = docusign_esign.apis.users_api.UsersApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Adds news user to the specified account.
        """
        pass

    def test_create_signatures(self):
        """
        Test case for create_signatures

        Adds user Signature and initials images to a Signature.
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Removes users account privileges.
        """
        pass

    def test_delete_contact_with_id(self):
        """
        Test case for delete_contact_with_id

        Replaces a particular contact associated with an account for the DocuSign service.
        """
        pass

    def test_delete_contacts(self):
        """
        Test case for delete_contacts

        Delete contacts associated with an account for the DocuSign service.
        """
        pass

    def test_delete_custom_settings(self):
        """
        Test case for delete_custom_settings

        Deletes custom user settings for a specified user.
        """
        pass

    def test_delete_profile_image(self):
        """
        Test case for delete_profile_image

        Deletes the user profile image for the specified user.
        """
        pass

    def test_delete_signature(self):
        """
        Test case for delete_signature

        Removes removes signature information for the specified user.
        """
        pass

    def test_delete_signature_image(self):
        """
        Test case for delete_signature_image

        Deletes the user initials image or the  user signature image for the specified user.
        """
        pass

    def test_get_contact_by_id(self):
        """
        Test case for get_contact_by_id

        Gets a particular contact associated with the user's account.
        """
        pass

    def test_get_information(self):
        """
        Test case for get_information

        Gets the user information for a specified user.
        """
        pass

    def test_get_profile(self):
        """
        Test case for get_profile

        Retrieves the user profile for a specified user.
        """
        pass

    def test_get_profile_image(self):
        """
        Test case for get_profile_image

        Retrieves the user profile image for the specified user.
        """
        pass

    def test_get_settings(self):
        """
        Test case for get_settings

        Gets the user account settings for a specified user.
        """
        pass

    def test_get_signature(self):
        """
        Test case for get_signature

        Gets the user signature information for the specified user.
        """
        pass

    def test_get_signature_image(self):
        """
        Test case for get_signature_image

        Retrieves the user initials image or the  user signature image for the specified user.
        """
        pass

    def test_list(self):
        """
        Test case for list

        Retrieves the list of users for the specified account.
        """
        pass

    def test_list_custom_settings(self):
        """
        Test case for list_custom_settings

        Retrieves the custom user settings for a specified user.
        """
        pass

    def test_list_signatures(self):
        """
        Test case for list_signatures

        Retrieves a list of user signature definitions for a specified user.
        """
        pass

    def test_post_contacts(self):
        """
        Test case for post_contacts

        Imports multiple new contacts into the contacts collection from CSV, JSON, or XML (based on content type).
        """
        pass

    def test_put_contacts(self):
        """
        Test case for put_contacts

        Replaces contacts associated with an account for the DocuSign service.
        """
        pass

    def test_update_custom_settings(self):
        """
        Test case for update_custom_settings

        Adds or updates custom user settings for the specified user.
        """
        pass

    def test_update_profile(self):
        """
        Test case for update_profile

        Updates the user profile information for the specified user.
        """
        pass

    def test_update_profile_image(self):
        """
        Test case for update_profile_image

        Updates the user profile image for a specified user.
        """
        pass

    def test_update_settings(self):
        """
        Test case for update_settings

        Updates the user account settings for a specified user.
        """
        pass

    def test_update_signature(self):
        """
        Test case for update_signature

        Updates the user signature for a specified user.
        """
        pass

    def test_update_signature_image(self):
        """
        Test case for update_signature_image

        Updates the user signature image or user initials image for the specified user.
        """
        pass

    def test_update_signatures(self):
        """
        Test case for update_signatures

        Adds/updates a user signature.
        """
        pass

    def test_update_user(self):
        """
        Test case for update_user

        Updates the specified user information.
        """
        pass

    def test_update_users(self):
        """
        Test case for update_users

        Change one or more user in the specified account.
        """
        pass


if __name__ == '__main__':
    unittest.main()
