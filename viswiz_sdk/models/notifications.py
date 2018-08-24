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


class Notifications(object):
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
        'email_enabled': 'bool',
        'slack_enabled': 'bool',
        'slack_url': 'str'
    }

    attribute_map = {
        'email_enabled': 'emailEnabled',
        'slack_enabled': 'slackEnabled',
        'slack_url': 'slackURL'
    }

    def __init__(self, email_enabled=None, slack_enabled=None, slack_url=None):  # noqa: E501
        """Notifications - a model defined in Swagger"""  # noqa: E501

        self._email_enabled = None
        self._slack_enabled = None
        self._slack_url = None
        self.discriminator = None

        if email_enabled is not None:
            self.email_enabled = email_enabled
        if slack_enabled is not None:
            self.slack_enabled = slack_enabled
        if slack_url is not None:
            self.slack_url = slack_url

    @property
    def email_enabled(self):
        """Gets the email_enabled of this Notifications.  # noqa: E501

        Controls if email reports are sent on new builds  # noqa: E501

        :return: The email_enabled of this Notifications.  # noqa: E501
        :rtype: bool
        """
        return self._email_enabled

    @email_enabled.setter
    def email_enabled(self, email_enabled):
        """Sets the email_enabled of this Notifications.

        Controls if email reports are sent on new builds  # noqa: E501

        :param email_enabled: The email_enabled of this Notifications.  # noqa: E501
        :type: bool
        """

        self._email_enabled = email_enabled

    @property
    def slack_enabled(self):
        """Gets the slack_enabled of this Notifications.  # noqa: E501

        Controls if Slack notifications are sent on new builds  # noqa: E501

        :return: The slack_enabled of this Notifications.  # noqa: E501
        :rtype: bool
        """
        return self._slack_enabled

    @slack_enabled.setter
    def slack_enabled(self, slack_enabled):
        """Sets the slack_enabled of this Notifications.

        Controls if Slack notifications are sent on new builds  # noqa: E501

        :param slack_enabled: The slack_enabled of this Notifications.  # noqa: E501
        :type: bool
        """

        self._slack_enabled = slack_enabled

    @property
    def slack_url(self):
        """Gets the slack_url of this Notifications.  # noqa: E501

        The Slack webhook URL to use for sending notifications  # noqa: E501

        :return: The slack_url of this Notifications.  # noqa: E501
        :rtype: str
        """
        return self._slack_url

    @slack_url.setter
    def slack_url(self, slack_url):
        """Sets the slack_url of this Notifications.

        The Slack webhook URL to use for sending notifications  # noqa: E501

        :param slack_url: The slack_url of this Notifications.  # noqa: E501
        :type: str
        """

        self._slack_url = slack_url

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
        if not isinstance(other, Notifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
