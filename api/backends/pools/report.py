from ramos.mixins import DefaultBackendMixin
from ramos.pool import BackendPool


class ReportBackendPool(DefaultBackendMixin, BackendPool):
    backend_type = 'report'
    SETTINGS_KEY = 'DEFAULT_REPORT_BACKEND'
