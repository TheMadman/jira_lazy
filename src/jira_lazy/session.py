"""@package jira_lazy
"""

from typing import Any
import requests

class Session:
    """Represents a single, persistent session to the Jira server.

    Used to perform raw JSON requests/responses with no additional
    processing.
    """

    def __init__(
            self,
            base_url: str,
            basic_auth: tuple[str, str],
            version: str = "2"):
        """Constructs a session with a Jira REST API.

        @param base_url The URL for the server, e.g. https://your-org.atlassian.net
        @param basic_auth Your authentication details, usually your E-mail address and a
            token. Consult https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
            for creating an API token to use.
        @param version The API version to use. Defaults to version 2.
        """
        self.__basic_auth = requests.auth.HTTPBasicAuth(*basic_auth)
        self.__api_url = f"{base_url}/rest/api/{version}"

    def __url(self, path: str) -> str:
        return f"{self.__api_url}/{path}"

    def get(self, path: str, *args, **kwargs) -> Any:
        """Performs a get request, parsing the result as JSON and returning it.

        The path can be a format string, in which case additional arguments will
        be substituted in.

        Example:

        >>> session = Session("https://jira.atlassian.net", auth_details)
        >>> session.get("issue/{}", 1) # becomes "issue/1"
        ... { "response" }

        Keyword arguments are passed directly to requests.get.

        @param path The path to get.
        
        @returns The parsed JSON response.
        """
        return requests.get(self.__url(path.format(*args)), auth=self.__basic_auth, **kwargs).json()

    def post(self, path: str, data: dict, **kwargs) -> Any:
        """Performs a post request.

        Additional keyword arguments are passed as-is to requests.post.

        @param path The path to post to.
        @param data The data to send in the request body.

        @returns The parsed JSON response.
        """
        return requests.post(self.__url(path), auth=self.__basic_auth, data=data, **kwargs).json()
