import requests


def check_route(url, word):
    # Sends an HTTP GET request to the specified URL
    rq = requests.get(f"{url}{word}")

    # Checks if the status code of the response is not equal to 404
    if rq.status_code != 404:
        # Returns the URL if the corresponding resource is found on the server
        return f"{url}{word}"
