# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomTabsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, account_id, **kwargs):
        """
        Creates a custom tab.
        Creates a tab with pre-defined properties, such as a text tab with a certain font type and validation pattern. Users can access the custom tabs when sending documents through the DocuSign web application.  Custom tabs can be created for approve, checkbox, company, date, date signed, decline, email, email address, envelope ID, first name, formula, full name, initial here, last name, list, note, number, radio, sign here, signer attachment, SSN, text, title, and zip tabs.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param TabMetadata tab_metadata:
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_with_http_info(account_id, **kwargs)
            return data

    def create_with_http_info(self, account_id, **kwargs):
        """
        Creates a custom tab.
        Creates a tab with pre-defined properties, such as a text tab with a certain font type and validation pattern. Users can access the custom tabs when sending documents through the DocuSign web application.  Custom tabs can be created for approve, checkbox, company, date, date signed, decline, email, email address, envelope ID, first name, formula, full name, initial here, last name, list, note, number, radio, sign here, signer attachment, SSN, text, title, and zip tabs.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param TabMetadata tab_metadata:
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'tab_metadata']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/tab_definitions'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tab_metadata' in params:
            body_params = params['tab_metadata']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TabMetadata',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete(self, account_id, custom_tab_id, **kwargs):
        """
        Deletes custom tab information.
        Deletes the custom from the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(account_id, custom_tab_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(account_id, custom_tab_id, **kwargs)
            return data

    def delete_with_http_info(self, account_id, custom_tab_id, **kwargs):
        """
        Deletes custom tab information.
        Deletes the custom from the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'custom_tab_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete`")
        # verify the required parameter 'custom_tab_id' is set
        if ('custom_tab_id' not in params) or (params['custom_tab_id'] is None):
            raise ValueError("Missing the required parameter `custom_tab_id` when calling `delete`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/tab_definitions/{customTabId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'custom_tab_id' in params:
            path_params['customTabId'] = params['custom_tab_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get(self, account_id, custom_tab_id, **kwargs):
        """
        Gets custom tab information.
        Retrieves information about the requested custom tab on the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(account_id, custom_tab_id, **kwargs)
        else:
            (data) = self.get_with_http_info(account_id, custom_tab_id, **kwargs)
            return data

    def get_with_http_info(self, account_id, custom_tab_id, **kwargs):
        """
        Gets custom tab information.
        Retrieves information about the requested custom tab on the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'custom_tab_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get`")
        # verify the required parameter 'custom_tab_id' is set
        if ('custom_tab_id' not in params) or (params['custom_tab_id'] is None):
            raise ValueError("Missing the required parameter `custom_tab_id` when calling `get`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/tab_definitions/{customTabId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'custom_tab_id' in params:
            path_params['customTabId'] = params['custom_tab_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TabMetadata',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, account_id, **kwargs):
        """
        Gets a list of all account tabs.
        Retrieves a list of all tabs associated with the account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_only: When set to **true**, only custom tabs are returned in the response. 
        :return: TabMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(account_id, **kwargs)
        else:
            (data) = self.list_with_http_info(account_id, **kwargs)
            return data

    def list_with_http_info(self, account_id, **kwargs):
        """
        Gets a list of all account tabs.
        Retrieves a list of all tabs associated with the account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_only: When set to **true**, only custom tabs are returned in the response. 
        :return: TabMetadataList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'custom_tab_only']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/tab_definitions'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'custom_tab_only' in params:
            query_params['custom_tab_only'] = params['custom_tab_only']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TabMetadataList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, account_id, custom_tab_id, **kwargs):
        """
        Updates custom tab information.  
        Updates the information in a custom tab for the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :param TabMetadata tab_metadata:
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(account_id, custom_tab_id, **kwargs)
        else:
            (data) = self.update_with_http_info(account_id, custom_tab_id, **kwargs)
            return data

    def update_with_http_info(self, account_id, custom_tab_id, **kwargs):
        """
        Updates custom tab information.  
        Updates the information in a custom tab for the specified account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(account_id, custom_tab_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str custom_tab_id: (required)
        :param TabMetadata tab_metadata:
        :return: TabMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'custom_tab_id', 'tab_metadata']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update`")
        # verify the required parameter 'custom_tab_id' is set
        if ('custom_tab_id' not in params) or (params['custom_tab_id'] is None):
            raise ValueError("Missing the required parameter `custom_tab_id` when calling `update`")


        collection_formats = {}

        resource_path = '/v2/accounts/{accountId}/tab_definitions/{customTabId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'custom_tab_id' in params:
            path_params['customTabId'] = params['custom_tab_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tab_metadata' in params:
            body_params = params['tab_metadata']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TabMetadata',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
