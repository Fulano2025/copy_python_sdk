# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from meli.configuration import Configuration


class VariationsAttributeCombinations(object):
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
        'name': 'str',
        'value_id': 'str',
        'value_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value_id': 'value_id',
        'value_name': 'value_name'
    }

    def __init__(self, name=None, value_id=None, value_name=None, local_vars_configuration=None):  # noqa: E501
        """VariationsAttributeCombinations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value_id = None
        self._value_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value_id is not None:
            self.value_id = value_id
        if value_name is not None:
            self.value_name = value_name

    @property
    def name(self):
        """Gets the name of this VariationsAttributeCombinations.  # noqa: E501


        :return: The name of this VariationsAttributeCombinations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariationsAttributeCombinations.


        :param name: The name of this VariationsAttributeCombinations.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value_id(self):
        """Gets the value_id of this VariationsAttributeCombinations.  # noqa: E501


        :return: The value_id of this VariationsAttributeCombinations.  # noqa: E501
        :rtype: str
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this VariationsAttributeCombinations.


        :param value_id: The value_id of this VariationsAttributeCombinations.  # noqa: E501
        :type: str
        """

        self._value_id = value_id

    @property
    def value_name(self):
        """Gets the value_name of this VariationsAttributeCombinations.  # noqa: E501


        :return: The value_name of this VariationsAttributeCombinations.  # noqa: E501
        :rtype: str
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        """Sets the value_name of this VariationsAttributeCombinations.


        :param value_name: The value_name of this VariationsAttributeCombinations.  # noqa: E501
        :type: str
        """

        self._value_name = value_name

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
        if not isinstance(other, VariationsAttributeCombinations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VariationsAttributeCombinations):
            return True

        return self.to_dict() != other.to_dict()
