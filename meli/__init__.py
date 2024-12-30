# coding: utf-8

# flake8: noqa

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from meli.api.categories_api import CategoriesApi
from meli.api.items_api import ItemsApi
from meli.api.items_health_api import ItemsHealthApi
from meli.api.o_auth_2_0_api import OAuth20Api
from meli.api.rest_client_api import RestClientApi

# import ApiClient
from meli.api_client import ApiClient
from meli.configuration import Configuration
from meli.exceptions import OpenApiException
from meli.exceptions import ApiTypeError
from meli.exceptions import ApiValueError
from meli.exceptions import ApiKeyError
from meli.exceptions import ApiException
# import models into sdk package
from meli.models.attributes import Attributes
from meli.models.attributes_value_struct import AttributesValueStruct
from meli.models.attributes_values import AttributesValues
from meli.models.inline_object import InlineObject
from meli.models.item import Item
from meli.models.item_pictures import ItemPictures
from meli.models.variations import Variations
from meli.models.variations_attribute_combinations import VariationsAttributeCombinations

