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


class DashboardColor(object):
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
        'id': 'str',
        'type': 'str',
        'hex': 'str',
        'name': 'str',
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'hex': 'hex',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, id=None, type=None, hex=None, name=None, value=None):  # noqa: E501
        """DashboardColor - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._hex = None
        self._name = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.hex = hex
        self.name = name
        self.value = value

    @property
    def id(self):
        """Gets the id of this DashboardColor.  # noqa: E501

        ID is the unique id of the view color  # noqa: E501

        :return: The id of this DashboardColor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardColor.

        ID is the unique id of the view color  # noqa: E501

        :param id: The id of this DashboardColor.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this DashboardColor.  # noqa: E501

        Type is how the color is used.  # noqa: E501

        :return: The type of this DashboardColor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DashboardColor.

        Type is how the color is used.  # noqa: E501

        :param type: The type of this DashboardColor.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["min", "max", "threshold", "scale", "text", "background"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def hex(self):
        """Gets the hex of this DashboardColor.  # noqa: E501

        Hex is the hex number of the color  # noqa: E501

        :return: The hex of this DashboardColor.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this DashboardColor.

        Hex is the hex number of the color  # noqa: E501

        :param hex: The hex of this DashboardColor.  # noqa: E501
        :type: str
        """
        if hex is None:
            raise ValueError("Invalid value for `hex`, must not be `None`")  # noqa: E501
        if hex is not None and len(hex) > 7:
            raise ValueError("Invalid value for `hex`, length must be less than or equal to `7`")  # noqa: E501
        if hex is not None and len(hex) < 7:
            raise ValueError("Invalid value for `hex`, length must be greater than or equal to `7`")  # noqa: E501

        self._hex = hex

    @property
    def name(self):
        """Gets the name of this DashboardColor.  # noqa: E501

        Name is the user-facing name of the hex color  # noqa: E501

        :return: The name of this DashboardColor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardColor.

        Name is the user-facing name of the hex color  # noqa: E501

        :param name: The name of this DashboardColor.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this DashboardColor.  # noqa: E501

        Value is the data value mapped to this color  # noqa: E501

        :return: The value of this DashboardColor.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DashboardColor.

        Value is the data value mapped to this color  # noqa: E501

        :param value: The value of this DashboardColor.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, DashboardColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
