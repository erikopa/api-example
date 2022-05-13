from ramos.mixins import ThreadSafeCreateMixin

from api.backends.report.backend import ReportBackend
from api.backends.report.exceptions import ReportBackendError


class FakeReportBackend(ThreadSafeCreateMixin, ReportBackend):
    id = 'fake-report'

    async def get_report(self, data: str) -> str:
        return 'this is a fake report'


class FakeReportErrorBackend(ThreadSafeCreateMixin, ReportBackend):
    id = 'fake-report-error'

    async def get_report(self, data: str) -> str:
        raise ReportBackendError(error_message='Fake report error')
