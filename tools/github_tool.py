import requests

def search_repositories(query):
    """
    Searches public GitHub repositories using GitHub REST API (no auth).
    """
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 3
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return {"error": "GitHub API failed"}

    data = response.json()
    results = []

    for repo in data.get("items", []):
        results.append({
            "name": repo["name"],
            "description": repo["description"],
            "stars": repo["stargazers_count"]
        })

    return results
