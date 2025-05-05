import requests

urls = [
    "https://httpstat.us/100",
    "https://httpstat.us/200",
    "https://httpstat.us/300",
    "https://httpstat.us/400",
    "https://httpstat.us/500"
]


# Функция обработки ответа
def handle_response(status_code):
    if 100 <= status_code < 200:
        return f"{status_code} Informational: Informational responses, request continues."
    elif 200 <= status_code < 300:
        return f"{status_code} Success: The request was successfully received, understood, and accepted."
    elif 300 <= status_code < 400:
        return f"{status_code} Redirection: The client must take additional action to complete the request."
    elif 400 <= status_code < 500:
        return f"{status_code} Client Error: The request contains bad syntax or cannot be fulfilled."
    elif 500 <= status_code < 600:
        return f"{status_code} Server Error: The server failed to fulfill a valid request."
    else:
        return f"Unexpected Status Code: {status_code}"


def fetch_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        print(f"URL: {url}")
        print(f"Status Code: {status_code}")
        print(f"Response Body: {response.text}\n")

        print(handle_response(status_code))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


for url in urls:
    fetch_status(url)
