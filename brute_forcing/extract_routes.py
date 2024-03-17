import multiprocessing

import requests
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import os
import time
from brute_forcing.check_routes import check_route
from config.config import BASE_URL


def extract_routes(dir_list):
    cpu_count = multiprocessing.cpu_count()

    with open(dir_list, 'rb') as file:
        lines = file.readlines()

        with ThreadPoolExecutor(max_workers=cpu_count) as executor:
            futures = []
            batch_size = 10
            for i in range(0, len(lines), batch_size):
                batch = lines[i:i + batch_size]
                batch_futures = []
                for line in batch:
                    word = line.decode('utf-8').strip()
                    print(f"Checking path: /{word}")
                    batch_futures.append(executor.submit(check_route, BASE_URL, word))
                futures.append(batch_futures)

            for batch_futures in futures:
                for future in concurrent.futures.as_completed(batch_futures):
                    result = future.result()
                    if result:
                        print(f"{result}: exists")
