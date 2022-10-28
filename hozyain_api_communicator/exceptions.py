import typing


class HozyainAPIException(Exception):
    """
    Every HOZYAIN.API exceptions is inherited from this.

    Use it if you want to catch all error from this project.
    """


class ExceptionConfigurationError(HozyainAPIException):
    """Exception that is executed every time when custom exceptions is used incorrectly"""


class HozyainAPIError(HozyainAPIException):
    """
    Base HOZYAIN.API exception to catch every possible error.
    Every other HOZYAIN.API exceptions is inherited from this.
    """
    default_message: typing.Optional[str]
    default_error_code: typing.Optional[int]

    def __init__(self, message: typing.Optional[str], error_code: typing.Optional[int]):
        # Check so either default message or passed message is not None
        if message is None and self.default_message is None:
            raise ExceptionConfigurationError(f'Exception "{self.__class__.__name__}" has no message!')

        # Check so either default error code or passed error code is not None
        if error_code is None and self.default_error_code is None:
            raise ExceptionConfigurationError(f'Exception "{self.__class__.__name__}" has no error code!')

        # Save error information into self
        if message is None:
            self.message = self.default_message
        else:
            self.message = message

        if error_code is None:
            self.error_code = self.default_error_code
        else:
            self.error_code = error_code

        super().__init__(message)


class HozyainAPIConnectionError(HozyainAPIError):
    """Executed when failed to connect to the HOZYAIN.API"""
    default_error_code = 503


class HozyainAPIBadRequestError(HozyainAPIError):
    """Executed when receiving 400 error from the HOZYAIN.API"""
    default_error_code = 400


class HozyainAPIInternalError(HozyainAPIError):
    """Executed, when error is related to the server itself"""
    default_error_code: int = 500


class HozyainAPIConfigurationError(HozyainAPIException):
    pass


class ImproperServiceConfigurationError(Exception):
    """Executed, when HOZYAIN.API communicator service is improperly configured"""

