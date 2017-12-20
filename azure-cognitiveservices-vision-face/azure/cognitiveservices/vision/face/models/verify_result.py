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


class VerifyResult(Model):
    """Result of the verify operation.

    :param is_identical: True if the two faces belong to the same person or
     the face belongs to the person, otherwise false.
    :type is_identical: bool
    :param confidence:
    :type confidence: float
    """

    _validation = {
        'is_identical': {'required': True},
    }

    _attribute_map = {
        'is_identical': {'key': 'isIdentical', 'type': 'bool'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(self, is_identical, confidence=None):
        self.is_identical = is_identical
        self.confidence = confidence