"""@package jira_lazy
"""

from jira_lazy.session import Session
from jira_lazy.collection_endpoint import CollectionEndpoint, PageParseException

def issue_search(
        session: Session,
        jql: str,
        startAt: int = 0,
        maxResults: int = 100,
        fields: list[str]|None = None,
        expand: str = "",
        properties: list[str]|None = None,
        fieldsByKeys: bool = False) -> CollectionEndpoint:

    params = {
            "jql": jql,
            "expand": expand,
            "properties": properties,
            "fieldsByKeys": fieldsByKeys,
    }
    if fields is not None:
        params['fields'] = fields
    return CollectionEndpoint(
            session,
            "search",
            startAt,
            maxResults,
            params=params,
            fieldName="issues")

def issue_changelog(
        session: Session,
        issue_id: str,
        startAt: int = 0,
        maxResults: int = 100) -> CollectionEndpoint:
    return CollectionEndpoint(
            session,
            f"issue/{issue_id}/changelog",
            startAt,
            maxResults)
