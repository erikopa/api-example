class BaseBackendException(Exception):
    http_status = 500
    error_message = 'Internal Server Error'

    def __init__(self, http_status=None, error_message=None):
        if http_status:
            self.http_status = http_status
        if error_message:
            self.error_message = error_message

    def __str__(self):
        return (
            f'{self.__class__.__name__}: '
            f'{self.http_status} - {self.error_message}'
        )
