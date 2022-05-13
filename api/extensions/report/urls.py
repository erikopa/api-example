from aiohttp import web

from api.extensions.report import views


def build_urls(prefix=''):
    return [
        web.view(
            f'{prefix}/report', views.ReportViews
        ),
        web.view(
            f'{prefix}/report/{{backend_id}}', views.ReportViews
        ),
    ]
