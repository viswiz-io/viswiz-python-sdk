# coding: utf-8

"""
    VisWiz.io API Documentation

    This SDK allows you to query and create new projects, builds or images within the VisWiz service.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: support@viswiz.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from viswiz_sdk.models.build import Build  # noqa: F401,E501
from viswiz_sdk.models.build_results_images import BuildResultsImages  # noqa: F401,E501


class BuildResults(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'build': 'Build',
        'comparison_build': 'Build',
        'images': 'list[BuildResultsImages]'
    }

    attribute_map = {
        'build': 'build',
        'comparison_build': 'comparisonBuild',
        'images': 'images'
    }

    def __init__(self, build=None, comparison_build=None, images=None):  # noqa: E501
        """BuildResults - a model defined in Swagger"""  # noqa: E501

        self._build = None
        self._comparison_build = None
        self._images = None
        self.discriminator = None

        if build is not None:
            self.build = build
        if comparison_build is not None:
            self.comparison_build = comparison_build
        if images is not None:
            self.images = images

    @property
    def build(self):
        """Gets the build of this BuildResults.  # noqa: E501


        :return: The build of this BuildResults.  # noqa: E501
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this BuildResults.


        :param build: The build of this BuildResults.  # noqa: E501
        :type: Build
        """

        self._build = build

    @property
    def comparison_build(self):
        """Gets the comparison_build of this BuildResults.  # noqa: E501


        :return: The comparison_build of this BuildResults.  # noqa: E501
        :rtype: Build
        """
        return self._comparison_build

    @comparison_build.setter
    def comparison_build(self, comparison_build):
        """Sets the comparison_build of this BuildResults.


        :param comparison_build: The comparison_build of this BuildResults.  # noqa: E501
        :type: Build
        """

        self._comparison_build = comparison_build

    @property
    def images(self):
        """Gets the images of this BuildResults.  # noqa: E501

        The list of images resulted from the comparison (both identical and different)  # noqa: E501

        :return: The images of this BuildResults.  # noqa: E501
        :rtype: list[BuildResultsImages]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this BuildResults.

        The list of images resulted from the comparison (both identical and different)  # noqa: E501

        :param images: The images of this BuildResults.  # noqa: E501
        :type: list[BuildResultsImages]
        """

        self._images = images

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BuildResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other