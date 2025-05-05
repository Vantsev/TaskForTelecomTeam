import requests

urls = [
    "https://httpstat.us/200",
    "https://httpstat.us/400",
    "https://httpstat.us/404",
    "https://httpstat.us/500"
]

def fetch_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        print(f"Status Code: {status_code}")
        print(f"Response Body: {response.text}\n")

        if 200 <= status_code <= 202:
            print(f"Request to {url} was successful\n")
        elif 400 <= status_code < 600:
            print(f"Error with status code {status_code} on {url}\n")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


for url in urls:
    fetch_status(url)
