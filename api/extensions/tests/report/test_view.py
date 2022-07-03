from aiohttp.abc import Application
from aiohttp.test_utils import AioHTTPTestCase
from api.factory import build_app


class ReportViewTestCase(AioHTTPTestCase):
    async def get_application(self) -> Application:
        return build_app()

    async def test_api(self):
        async with self.client.request("GET", "/report") as resp:
            self.assertEqual(resp.status, 200)
