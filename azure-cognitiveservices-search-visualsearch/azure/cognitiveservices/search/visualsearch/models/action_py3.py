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

from .creative_work import CreativeWork


class Action(CreativeWork):
    """Action.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageAction

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.visualsearch.models.Thing]
    :ivar date_published: The date on which the CreativeWork was published.
    :vartype date_published: str
    :ivar text: Text content of this creative work.
    :vartype text: str
    :ivar result: The result produced in the action.
    :vartype result:
     list[~azure.cognitiveservices.search.visualsearch.models.Thing]
    :ivar display_name: A display name for the action.
    :vartype display_name: str
    :ivar is_top_action: A Boolean representing whether this result is the top
     action.
    :vartype is_top_action: bool
    :ivar service_url: Use this URL to get additional data to determine how to
     take the appropriate action. For example, the serviceUrl might return JSON
     along with an image URL.
    :vartype service_url: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'date_published': {'readonly': True},
        'text': {'readonly': True},
        'result': {'readonly': True},
        'display_name': {'readonly': True},
        'is_top_action': {'readonly': True},
        'service_url': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'date_published': {'key': 'datePublished', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'result': {'key': 'result', 'type': '[Thing]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_top_action': {'key': 'isTopAction', 'type': 'bool'},
        'service_url': {'key': 'serviceUrl', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'ImageAction': 'ImageAction'}
    }

    def __init__(self, **kwargs) -> None:
        super(Action, self).__init__(**kwargs)
        self.result = None
        self.display_name = None
        self.is_top_action = None
        self.service_url = None
        self._type = 'Action'
