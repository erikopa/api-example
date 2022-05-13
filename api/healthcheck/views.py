from aiohttp import web

from api.contrib.response import JSONResponse


class HealthCheckView(web.View):
    skip_auth = True

    async def get(self):
        return JSONResponse(data={'status': 'OK'})
