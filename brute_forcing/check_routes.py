import requests


def check_route(url, word):
    rq = requests.get(f"{url}{word}")
    if rq.status_code != 404:
        return f"{url}{word}"
