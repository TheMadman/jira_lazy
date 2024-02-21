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

## Don't I have to do pagination stuff though?

No.

## Does it fetch all the pages at once?

No.

## You haven't added a function for an endpoint I need, how do I write my own?

Use `jira_lazy.collection_endpoint.CollectionEndpoint`.
