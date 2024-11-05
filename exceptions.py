# 400: An issue with the contents of the request (e.g. a required parameter is missing)
class PostcoderParameterError(Exception):
    """Exception raised for custom errors with additional information."""

# 403: An issue with the API key or account (e.g. the API key is invalid or there are insufficient credits for the request)
class PostcoderAccountError(Exception):
    """Exception raised for custom errors with additional information."""

# 404: An issue with the structure of the request (e.g. the endpoint does not exist)
class PostcoderEndpointNotFoundError(Exception):
    """Exception raised for custom errors with additional information."""

# 405: 
class PostcoderMethodNotAllowedError(Exception):
    """Exception raised for custom errors with additional information."""

# 500: An issue with Postcoder
class PostcoderServerError(Exception):
    """Exception raised for custom errors with additional information."""

# JSON issues 
class PostcoderJSONError(Exception):
    """Exception raised for custom errors with additional information."""