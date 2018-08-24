# coding: utf-8

"""
    VisWiz.io API Documentation

    This SDK allows you to query and create new projects, builds or images within the VisWiz service.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: support@viswiz.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import viswiz_sdk
from Client.projects_api import ProjectsApi  # noqa: E501
from viswiz_sdk.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = Client.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a project  # noqa: E501
        """
        pass

    def test_get_project_notifications(self):
        """Test case for get_project_notifications

        Get notifications settings  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Get all projects  # noqa: E501
        """
        pass

    def test_update_project_notifications(self):
        """Test case for update_project_notifications

        Update notifications settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()