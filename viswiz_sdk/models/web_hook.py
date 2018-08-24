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


class WebHook(object):
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
        'created_at': 'datetime',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, created_at=None, name=None, url=None):  # noqa: E501
        """WebHook - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._name = None
        self._url = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def created_at(self):
        """Gets the created_at of this WebHook.  # noqa: E501

        The date and time the webhook was created  # noqa: E501

        :return: The created_at of this WebHook.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebHook.

        The date and time the webhook was created  # noqa: E501

        :param created_at: The created_at of this WebHook.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this WebHook.  # noqa: E501

        The webhook name  # noqa: E501

        :return: The name of this WebHook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebHook.

        The webhook name  # noqa: E501

        :param name: The name of this WebHook.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this WebHook.  # noqa: E501

        The webhook URL  # noqa: E501

        :return: The url of this WebHook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebHook.

        The webhook URL  # noqa: E501

        :param url: The url of this WebHook.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, WebHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
