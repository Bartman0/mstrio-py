import requests


def iserver_trustrelationship(connection, verbose=False):
    """
     Args:
        connection: MicroStrategy REST API connection object
        verbose (bool, optional): Verbosity of server responses; defaults to False.
    Returns:
        Complete HTTP response object
    """

    headers = {'Content-Type': 'application/json', 'X-MSTR-AuthToken': connection.auth_token}
    response = requests.get(connection.base_url + '/admin/restServerSettings/iServer/trustRelationship',
                            headers=headers, auth=connection.auth,
                            cookies=connection.cookies,
                            verify=connection.ssl_verify)

    if verbose:
        print(response.url)

    return response


def iserver_trustrelationship_set(connection, body={}, verbose=False):
    """
    Args:
        connection: MicroStrategy REST API connection object
        body (str): JSON-formatted definition of the URL or other unique identifier for the Web Server.
        verbose (bool, optional): Verbosity of server responses; defaults to False.
    Returns:
        Complete HTTP response object

    Body:
    {
        "webServerPath": "string"
    }
    """

    headers = {'Content-Type': 'application/json', 'X-MSTR-AuthToken': connection.auth_token}
    response = requests.post(url=connection.base_url + '/admin/restServerSettings/iServer/trustRelationship',
                             headers=headers, auth=connection.auth,
                             cookies=connection.cookies,
                             json=body,
                             verify=connection.ssl_verify)

    if verbose:
        print(response.url)

    return response


def iserver_trustrelationship_delete(connection, verbose=False):
    """
     Args:
        connection: MicroStrategy REST API connection object
        verbose (bool, optional): Verbosity of server responses; defaults to False.
    Returns:
        Complete HTTP response object
    """

    headers = {'Content-Type': 'application/json', 'X-MSTR-AuthToken': connection.auth_token}
    response = requests.delete(connection.base_url + '/admin/restServerSettings/iServer/trustRelationship',
                               headers=headers, auth=connection.auth,
                               cookies=connection.cookies,
                               verify=connection.ssl_verify)

    if verbose:
        print(response.url)

    return response


def restserversettings_auth(connection, verbose=False):
    """
     Args:
        connection: MicroStrategy REST API connection object
        verbose (bool, optional): Verbosity of server responses; defaults to False.
    Returns:
        Complete HTTP response object
    """

    headers = {'Content-Type': 'application/json', 'X-MSTR-AuthToken': connection.auth_token}
    response = requests.get(connection.base_url + '/api/admin/restServerSettings/auth',
                            headers=headers, auth=connection.auth,
                            cookies=connection.cookies,
                            verify=connection.ssl_verify)

    if verbose:
        print(response.url)

    return response


def restserversettings_auth_update(connection, body={}, verbose=False):
    """
    Args:
        connection: MicroStrategy REST API connection object
        body (str): JSON-formatted definition of the URL or other unique identifier for the Web Server.
        verbose (bool, optional): Verbosity of server responses; defaults to False.
    Returns:
        Complete HTTP response object

    Body:
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

    headers = {'Content-Type': 'application/json', 'X-MSTR-AuthToken': connection.auth_token}
    response = requests.post(url=connection.base_url + '/api/admin/restServerSettings/auth',
                             headers=headers, auth=connection.auth,
                             cookies=connection.cookies,
                             json=body,
                             verify=connection.ssl_verify)

    if verbose:
        print(response.url)

    return response
