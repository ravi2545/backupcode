import requests
url = "https://laptopsstore.atlassian.net/rest/api/3/issuetype"
headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth)

data = response.json()