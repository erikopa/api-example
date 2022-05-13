from aiohttp import web

from api.backends.pools.report import ReportBackendPool
from api.backends.report.exceptions import ReportBackendError
from api.contrib.response import JSONResponse
from api.extensions.report.exceptions import ReportException


class ReportViews(web.View):
    async def get(self):
        backend_id = self.request.match_info.get('backend_id')
        if backend_id:
            backend = ReportBackendPool.get(backend_id)
        else:
            backend = ReportBackendPool.get_default()

        try:
            response_data = await backend.get_report(data='this is a report')
        except ReportBackendError as e:
            report_exception = ReportException(
                http_status=e.http_status,
                error_message=e.error_message
            )
            return JSONResponse(
                data=report_exception.as_dict(),
                status=report_exception.http_status
            )
        return JSONResponse(data=response_data, status=200)
