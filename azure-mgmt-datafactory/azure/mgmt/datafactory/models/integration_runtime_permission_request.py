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


class IntegrationRuntimePermissionRequest(Model):
    """Grant or revoke access to integration runtime request.

    All required parameters must be populated in order to send to Azure.

    :param factory_identity: Required. The data factory identity.
    :type factory_identity: str
    """

    _validation = {
        'factory_identity': {'required': True},
    }

    _attribute_map = {
        'factory_identity': {'key': 'factoryIdentity', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IntegrationRuntimePermissionRequest, self).__init__(**kwargs)
        self.factory_identity = kwargs.get('factory_identity', None)
