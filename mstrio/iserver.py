from mstrio.api import system_administration


class WebserverPath(object):
    """WebserverPath class.

    Creates a webserver path object which is used to set the trust relationship value.
    """
    self._webserver_path = None

    def __init__(self, webserver_path):
        self._webserver_path = webserver_path

    def body(self):
        return {"webServerPath": self._webserver_path}

class Trust(object):
    """Trust relationship class.

    Creates a trust object which is used in subsequent requests and manages the Intelligence Server
    trust relationship setting.
    """
    self._connection = None
    self._webserver_path = None

    def __init__(self, connection, webserver_path):
        self._connection = connection
        self._webserver_path = WebserverPath(webserver_path)
    
    def get_relationship(self):
        """Retrieve the current value of the trust relationship."""
        response = system_administration.iserver_trustrelationship(connection=self._connection)

        if not response.ok:
            msg = "Failed to retrieve trust relationship."
            self.__response_handler(response=response, msg=msg)
        else:
            print("MicroStrategy Intelligence trust relationship was retrieved.")

    def set_relationship(self):
        """Set the trust relationship."""
        response = system_administration.iserver_trustrelationship_set(connection=self._connection, body=self._webserver_path.body())

        if not response.ok:
            msg = "Failed to set trust relationship."
            self.__response_handler(response=response, msg=msg)
        else:
            print("MicroStrategy Intelligence trust relationship was set.")

    def delete_relationship(self):
        """Delete the existing trust relationship."""
        response = system_administration.iserver_trustrelationship_delete(connection=self._connection)

        if not response.ok:
            msg = "Failed to delete trust relationship."
            self.__response_handler(response=response, msg=msg)
        else:
            print("MicroStrategy Intelligence trust relationship was deleted.")

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
