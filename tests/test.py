import os
from unittest import TestCase
from getgeo.geodata import GetGeoData, GetGeoBase


class TestApp(TestCase):
    def setUp(self) -> None:
        self.api_key = os.environ.get("API_KEY")

    def tearDown(self) -> None:
        self.api_key = None

    def test_geo_base(self):
        geo_data = GetGeoBase(self.api_key)  # type: ignore

        data = geo_data.get_my_geo_data()

        self.assertEqual(data["status"], "success")

    def test_geo_data(self):
        geo_data = GetGeoData(self.api_key)  # type: ignore

        # Google's IPv6 address
        # 2001:4860:4860::8888

        data = geo_data.get_geo_data("2001:4860:4860::8888")

        self.assertEqual(data["status"], "success")
