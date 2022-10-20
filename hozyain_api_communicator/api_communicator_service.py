import json

import requests
from gql.transport.websockets import WebsocketsTransport

from .exceptions import HozyainAPIConnectionError, ImproperServiceConfigurationError


class HozyainAPICommunicatorServiceMetaclass(type):
    """
    Metaclass that makes class on which it is applied a singleton.

    First time when class is instantiated its instance is saved into memory,
    so every other time when you will try to instantiate it __new__ method will return this instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(HozyainAPICommunicatorServiceMetaclass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HozyainAPICommunicatorService(metaclass=HozyainAPICommunicatorServiceMetaclass):
    """Service that is used to send requests to the HOZYAIN.API"""
    # TODO: Web-socket support
    # TODO: Authentication support
    url: str
    ws_transport: WebsocketsTransport

    def __init__(self, url: str = None):
        if url is None:
            raise ImproperServiceConfiguration('"url" is required argument!')
        # TODO: Validate api_url format
        self.url = url

        ws_url = f'ws{url[url.find(":"):]}'
        self.ws_transport = WebsocketsTransport(url=ws_url)

    def make_request(self, body: str):
        # TODO: Implement make request function
        # TODO: Add headers support

        try:
            r = requests.post(
                self.url,
                json={'query': body},
            )
        except requests.ConnectionError:
            raise HozyainAPIConnectionError('Failed to connect to the HOZYAIN.API server')

        return json.loads(r.text)
