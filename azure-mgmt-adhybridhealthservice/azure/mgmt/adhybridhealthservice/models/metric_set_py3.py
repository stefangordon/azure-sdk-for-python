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


class MetricSet(Model):
    """The set of metric values. Example of a MetricSet are Values of token
    requests for a Server1 or RelyingParty1.

    :param set_name: The name of the set.
    :type set_name: str
    :param values: The list of the metric values.
    :type values: list[int]
    """

    _attribute_map = {
        'set_name': {'key': 'setName', 'type': 'str'},
        'values': {'key': 'values', 'type': '[int]'},
    }

    def __init__(self, *, set_name: str=None, values=None, **kwargs) -> None:
        super(MetricSet, self).__init__(**kwargs)
        self.set_name = set_name
        self.values = values