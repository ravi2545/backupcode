import requests
from .basic_auth import auth

class Fields:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_fields(self):
        url = f"https://{self.base_url}.atlassian.net/rest/api/3/field/search"
        headers = {
            "Accept": "application/json"
        }

        # Initialize pagination parameters
        start_at = 0
        max_results = 50
        is_last = False
        all_values = []

        while not is_last:
            # Prepare the request with pagination
            params = {
                "startAt": start_at,
                "maxResults": max_results,
                "expand": "key,stableId,lastUsed,screensCount,contextsCount,isLocked,searcherKey"
            }

            # Make the request
            response = requests.get(url, headers=headers, params=params, auth=auth)

            # Parse the JSON response
            data = response.json()

            # Append the retrieved values to the all_values list
            all_values.extend(data.get('values', []))

            # Check if this is the last page
            is_last = data.get('isLast', False)

            # Update the startAt parameter for the next iteration
            start_at += max_results

        return all_values
    
    def get_issue_type(self):
        url = f"https://{self.base_url}.atlassian.net/rest/api/3/issuetype"
        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth)

        return response.json()