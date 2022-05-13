from aiohttp import web

from api.healthcheck.urls import build_urls as healthcheck_urls_builder
from api.extensions.report.urls import build_urls as report_build_urls
from api.urls import build_urls as api_urls_builder


def build_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    return app


def setup_routes(app: web.Application):
    app.add_routes(healthcheck_urls_builder())
    app.add_routes(api_urls_builder())
    app.add_routes(report_build_urls())
