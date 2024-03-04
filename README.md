# Jira Lazy

A lazy library for lazy developers.

Example usage:

```python
from jira_lazy import Session, issue_search

auth = "email@example.com", "<token>"
session = Session("https://your-domain.atlassian.net", auth)

for issue in issue_search(session, "project=XMPL"):
    print(issue["key"])
```

## What's the interface?

```python
Session(
    self,
    base_url: str,
    basic_auth: tuple[str, str],
    version: str = "2")
```

Returns an object that stores connection data and manages requests.

```python
issue_search(
    session: Session,
    jql: str,
    startAt: int = 0,
    maxResults: int = 100,
    fields: list[str]|None = None,
    expand: str = "",
    properties: list[str]|None = None,
    fieldsByKeys: bool = False) -> CollectionEndpoint
```

Performs JQL-based issue search. Returns an iterable of issues, as dictionaries.

```python
issue_changelog(
    session: Session,
    issue_id: str,
    startAt: int = 0,
    maxResults: int = 100) -> CollectionEndpoint
```

Fetches the changelog for the given issue ID. Returns an iterable of changelog entries as dictionaries.

Currently, these are the only functions implemented as part of the public interface.

## Don't I have to do pagination stuff though?

No.

## Does it fetch all the pages at once?

No.

## You haven't added a function for an endpoint I need, how do I write my own?

Use `jira_lazy.collection_endpoint.CollectionEndpoint`.
