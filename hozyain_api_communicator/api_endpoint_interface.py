import abc
import typing
import string

import pydantic

from .api_communicator_service import HozyainAPICommunicatorService
from .exceptions import HozyainAPIError, HozyainAPIBadRequestError, HozyainAPIConnectionError, HozyainAPIInternalError


class IHozyainAPIEndpoint(abc.ABC):
    """
    Interface for hozyain_api endpoint.

    Inheritance example:
        TODO

    Usage example:
        TODO
    """
    # TODO: HOZYAIN.API endpoint interface
    request: str
    response_type: typing.Type[pydantic.BaseModel]
    transform_response: typing.Callable[[dict], dict]

    @classmethod
    def make_request(cls, **vars):
        # Paste gql variables into request
        request = string.Template(cls.request)

        try:
            request = request.substitute(**vars)
        except KeyError as e:
            raise HozyainAPIBadRequestError(f'Argument {e} is required!')

        response = HozyainAPICommunicatorService().make_request(body=request)

        # Return error or response
        if response.get('errors', None) is not None:
            cls._raise_error_response(response['errors'][0])
        else:
            return cls._parse_response(response)

    @classmethod
    def _raise_error_response(cls, error: dict):
        """Parse error that has come from the HOZYAIN.API and raise it"""
        error_message = error['message']
        error_code = error.get('extensions', {}).get('code', 503)

        if 500 > error_code >= 400:
            raise HozyainAPIBadRequestError(
                message=error_message,
                error_code=error_code,
            )

        if error_code >= 500:
            raise HozyainAPIInternalError(
                message=error_message,
                error_code=error_code,
            )

        raise HozyainAPIError(
            message=error_message,
            error_code=error_code,
        )

    @classmethod
    def _parse_response(cls, data):
        data = data['data']

        if cls.transform_response is not None:
            data = cls.transform_response(data)

        return cls.response_type.parse_obj(data)
