import unittest
from unittest.mock import patch
from mstrio.api import authentication
from mstrio import microstrategy
from mstrio.api.system_administration import restserversettings_auth, iserver_trustrelationship

USERNAME = "Administrator"
PASSWORD = "********"
PROJECT_NAME = "Mailinfo"
BASE_URL = "https://env-170843.trial.cloud.microstrategy.com/MicroStrategyLibrary/api"


class TestSystemAdministration(unittest.TestCase):

    def setUp(self):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.PROJECT_NAME = PROJECT_NAME
        self.BASE_URL = BASE_URL
        self.COOKIES = "test-cookie"
        self.APPCODE = 64

    def test_restserversettings_auth(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME, ssl_verify=False)
        conn.connect()
        response = restserversettings_auth(conn, verbose=True)
        print(response)

    def test_iserver_trustrelationship(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME, ssl_verify=False)
        conn.connect()
        response = iserver_trustrelationship(conn, verbose=True)
        print(response)

if __name__ == '__main__':
    unittest.main()
