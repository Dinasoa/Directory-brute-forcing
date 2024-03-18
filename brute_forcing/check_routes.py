import requests


def check_route(url, word):
    """
       Here we are going to check either the URL specified resource is found on the server
       :param dir_list: wordlist path
       :param base_url: the target website
       :return: the existent route found
    """
    rq = requests.get(f"{url}{word}")
    if rq.status_code != 404:
        return f"{url}{word} found"
