import pytest
import allure
from Rookie_automation.apis.xl import xl_login,zckh

class Testcase():
    @classmethod
    def setup_class(cls):
        xl_login.login()

    def test_01(self):
        result = zckh.zckh()
        assert result == 200
