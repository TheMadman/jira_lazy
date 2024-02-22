"""@package jira_lazy
"""

from jira_lazy.session import Session


class PageParseException(Exception):
    pass

class CollectionEndpoint:
    """Represents an endpoint which returns a collection of items.

    This class implements the iterator interface, allowing use
    in for loops. It handles pagination automatically, using lazy-loading.

    This means, if you begin iterating and break before finishing the first
    page, only one page is requested; if you iterate the whole collection,
    every page is requested as needed.
    """

    def __init__(
            self,
            session: Session,
            path: str,
            startAt: int = 0,
            maxResults: int = 100,
            params: dict = {},
            fieldName: str = "values"):
        """Constructs a new CollectionEndpoint.

        @param session The session to use for queries.
        @param path The path the collection comes from.
        @param startAt The first item to start from.
        @param maxResults The total number of results to fetch per page.
        @param params Additional get parameters.
        @param fieldName The name of the field containing the actual array
            in the JSON response.
        """
        self.__session = session
        self.__path = path
        self.__params = params
        self.__fieldName = fieldName

        params.update({
                "startAt": startAt,
                "maxResults": maxResults,
        })
        response = session.get(path, params=params)

        try:
            self.startAt = response['startAt']
            self.maxResults = response['maxResults']
            self.total = response['total']
            self.values = response[fieldName]
        except KeyError:
            raise PageParseException(f"Unexpected response JSON: {response}")

    def __iter__(self):
        if not self.values:
            return

        for value in self.values:
            yield value

        if self.startAt + self.maxResults < self.total:
            next_page = CollectionEndpoint(
                    self.__session,
                    self.__path,
                    self.startAt + self.maxResults,
                    self.maxResults,
                    self.__params,
                    self.__fieldName)
            for value in next_page:
                yield value

    def __len__(self):
        return self.total
