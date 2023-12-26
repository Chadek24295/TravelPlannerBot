import requests

def fetch_travel_data(api_url, params):
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Returns the JSON response if successful
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")

# Example usage
api_url = 'https://api.example.com/data'
params = {'departure': departure, 'destination': destination, 'date': travel_date}
data = fetch_travel_data(api_url, params)
