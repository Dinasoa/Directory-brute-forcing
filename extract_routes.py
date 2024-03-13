import requests
import concurrent.futures
import os
import time


def extract_routes(dir_list):
    url = "http://127.0.0.1:5000/"
    cpu_count = os.cpu_count()

    with open(dir_list, 'rb') as file:
        lines = file.readlines()

        with concurrent.futures.ThreadPoolExecutor(max_workers=cpu_count) as executor:
            futures = []
            for line in lines:
                word = line.decode('utf-8').strip()
                print(f"Checking path: /{word}")
                futures.append(executor.submit(check_route, url, word))

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    print(f"{result}: exists")


def check_route(url, word):
    rq = requests.get(f"{url}{word}")
    if rq.status_code != 404:
        return f"{url}{word}"


if __name__ == "__main__":
    start_time = time.time()
    extract_routes("dir_list.txt")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
