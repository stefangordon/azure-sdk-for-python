# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Usage(Model):
    """The details about the usage of a particular limited resource.

    :param unit: The type of measurement for usage.
    :type unit: str
    :param current_value: The current usage.
    :type current_value: int
    :param limit: The maximum allowed usage.
    :type limit: int
    :param name: The details about the localizable name of the used resource.
    :type name: ~azure.mgmt.hdinsight.models.LocalizedName
    """

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'LocalizedName'},
    }

    def __init__(self, unit=None, current_value=None, limit=None, name=None):
        super(Usage, self).__init__()
        self.unit = unit
        self.current_value = current_value
        self.limit = limit
        self.name = name
