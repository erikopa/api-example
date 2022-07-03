from aiohttp import web

from api.healthcheck.views import HealthCheckView


def build_urls(prefix=''):
    return [
        web.view(f'{prefix}/healthcheck', HealthCheckView)
    ]
