from mstrio.api import system_administration


class RestServerSettingsAuth(object):
    """RestServerSettingsAuth class.

    Creates a REST server settings auth object which is used to set the auth configuration on the REST server.
    """
    self._trusted = None

    def __init__(self, trusted):
        self._trusted = trusted

    """
    {
      "availableModes": [
        0
      ],
      "defaultMode": 0,
      "saml": {
        "isUsher": true
      },
      "kerberos": {
        "config": "string",
        "keytab": "string",
        "principal": "string"
      },
      "trustedProvider": 0,
      "trusted": {
        "provider": 0
      }
    }
    """
    def body(self):
        return {"trusted": self._trusted}

class RestServerSettings(object):
    """RestServerSettings class.

    Creates a REST server settings object which is used in subsequent requests and manages the REST Server settings.
    """
    self._connection = None
    self._auth = None

    def __init__(self, connection, provider):
        self._connection = connection
        self._auth = RestServerSettingsAuth(provider)

    def get_auth(self):
        """Retrieve the current value of the auth settings."""
        response = system_administration.restserversettings_auth(connection=self._connection)

        if not response.ok:
            msg = "Failed to retrieve auth settings."
            self.__response_handler(response=response, msg=msg)
        else:
            print("MicroStrategy Intelligence auth settings were retrieved.")

    def set_auth(self):
        """Set the current value of the trust relationship."""
        response = system_administration.restserversettings_auth_update(connection=self._connection, body=self._auth.body())

        if not response.ok:
            msg = "Failed to set auth settings."
            self.__response_handler(response=response, msg=msg)
        else:
            print("MicroStrategy Intelligence auth settings were set.")

    @staticmethod
    def __response_handler(response, msg):
        """Generic error message handler for transactions against datasets.

        Args:
            response: Response object returned by HTTP request.
            msg (str): Message to print in addition to any server-generated error message(s).

        """

        if response.status_code == 204:
            warnings.warn(
                '204 No Content: The server successfully processed the request and is not returning any content.')
        else:
            res = response.json()
            print("I-Server Error %s, %s" % (res['code'], res['message']))
            response.raise_for_status()
