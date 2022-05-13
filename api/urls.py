from aiohttp import web

from api.contrib.response import JSONResponse


class Index(web.View):
    skip_auth = True

    async def get(self):
        return JSONResponse(data={'status': 'OK'})


def build_urls(prefix=''):
    return [
        web.view(f'{prefix}/', Index)
    ]
