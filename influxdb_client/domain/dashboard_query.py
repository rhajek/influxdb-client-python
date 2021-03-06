# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DashboardQuery(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'text': 'str',
        'edit_mode': 'QueryEditMode',
        'name': 'str',
        'builder_config': 'BuilderConfig'
    }

    attribute_map = {
        'text': 'text',
        'edit_mode': 'editMode',
        'name': 'name',
        'builder_config': 'builderConfig'
    }

    def __init__(self, text=None, edit_mode=None, name=None, builder_config=None):  # noqa: E501
        """DashboardQuery - a model defined in OpenAPI"""  # noqa: E501

        self._text = None
        self._edit_mode = None
        self._name = None
        self._builder_config = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if edit_mode is not None:
            self.edit_mode = edit_mode
        if name is not None:
            self.name = name
        if builder_config is not None:
            self.builder_config = builder_config

    @property
    def text(self):
        """Gets the text of this DashboardQuery.  # noqa: E501

        The text of the flux query  # noqa: E501

        :return: The text of this DashboardQuery.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DashboardQuery.

        The text of the flux query  # noqa: E501

        :param text: The text of this DashboardQuery.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def edit_mode(self):
        """Gets the edit_mode of this DashboardQuery.  # noqa: E501


        :return: The edit_mode of this DashboardQuery.  # noqa: E501
        :rtype: QueryEditMode
        """
        return self._edit_mode

    @edit_mode.setter
    def edit_mode(self, edit_mode):
        """Sets the edit_mode of this DashboardQuery.


        :param edit_mode: The edit_mode of this DashboardQuery.  # noqa: E501
        :type: QueryEditMode
        """

        self._edit_mode = edit_mode

    @property
    def name(self):
        """Gets the name of this DashboardQuery.  # noqa: E501


        :return: The name of this DashboardQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardQuery.


        :param name: The name of this DashboardQuery.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def builder_config(self):
        """Gets the builder_config of this DashboardQuery.  # noqa: E501


        :return: The builder_config of this DashboardQuery.  # noqa: E501
        :rtype: BuilderConfig
        """
        return self._builder_config

    @builder_config.setter
    def builder_config(self, builder_config):
        """Sets the builder_config of this DashboardQuery.


        :param builder_config: The builder_config of this DashboardQuery.  # noqa: E501
        :type: BuilderConfig
        """

        self._builder_config = builder_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, DashboardQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
