class ReportException(Exception):
    def __init__(self, http_status=None, error_message=None):
        self.http_status = http_status
        self.error_message = error_message
        self.error_type = self._get_error_type(http_status)

    def _get_error_type(self, http_status):
        error_type_map = {
            503: 'Service Unavailable'
        }

        return error_type_map[http_status]

    def as_dict(self):
        return {
            'code': self.http_status,
            'error': self.error_type,
            'message': self.error_message
        }
