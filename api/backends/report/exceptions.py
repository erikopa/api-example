from api.backends.exception import BaseBackendException


class ReportBackendError(BaseBackendException):
    http_status = 503
    error_message = 'Report Unavailable'
