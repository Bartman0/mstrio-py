import unittest
from unittest.mock import patch

from requests.auth import HTTPBasicAuth

from mstrio.api import authentication
from mstrio import microstrategy
from mstrio.api.system_administration import restserversettings_auth, iserver_trustrelationship
from mstrio.iserver import Trust

USERNAME = "Administrator"
PASSWORD = "********"
PROJECT_NAME = "Mailinfo"
BASE_URL = "https://env-170843.trial.cloud.microstrategy.com/MicroStrategyLibrary/api"
BASIC_USERNAME="mstr"
BASIC_PASSWORD="********"


class TestSystemAdministration(unittest.TestCase):

    def setUp(self):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.PROJECT_NAME = PROJECT_NAME
        self.BASE_URL = BASE_URL
        self.BASIC_USERNAME=BASIC_USERNAME
        self.BASIC_PASSWORD=BASIC_PASSWORD
        self.COOKIES = "test-cookie"
        self.APPCODE = 64

    def test_restserversettings_auth(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME,
                                        auth=HTTPBasicAuth(self.BASIC_USERNAME, self.BASIC_PASSWORD),
                                        ssl_verify=False)
        conn.connect()
        response = restserversettings_auth(conn, verbose=True)
        print(response.content)

    def test_iserver_trustrelationship(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME,
                                        auth=HTTPBasicAuth(self.BASIC_USERNAME, self.BASIC_PASSWORD),
                                        ssl_verify=False)
        conn.connect()
        response = iserver_trustrelationship(conn, verbose=True)
        print(response.content)

    def test_trust_get_trustrelationship(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME,
                                        auth=HTTPBasicAuth(self.BASIC_USERNAME, self.BASIC_PASSWORD),
                                        ssl_verify=False)
        conn.connect()
        response = Trust(conn).get_relationship()
        print(response.content)

    def test_trust_set_trustrelationship(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME,
                                        auth=HTTPBasicAuth(self.BASIC_USERNAME, self.BASIC_PASSWORD),
                                        ssl_verify=False)
        conn.connect()
        response = Trust(conn, "https://iserver.test.com/blabla").set_relationship()
        print(response.content)

    def test_trust_delete_trustrelationship(self):
        conn = microstrategy.Connection(base_url=self.BASE_URL, username=self.USERNAME,
                                        password=self.PASSWORD, project_name=self.PROJECT_NAME,
                                        auth=HTTPBasicAuth(self.BASIC_USERNAME, self.BASIC_PASSWORD),
                                        ssl_verify=False)
        conn.connect()
        response = Trust(conn).delete_relationship()
        print(response.content)

if __name__ == '__main__':
    unittest.main()
