class BusinessException(Exception):
    """
    Base class for all business exceptions.
    """

    def __init__(
        self,
        message: str,
        status_code: int,
    ):
        self.message = message
        self.status_code = status_code

        super().__init__(message)