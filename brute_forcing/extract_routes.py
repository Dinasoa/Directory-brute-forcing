import multiprocessing

import requests
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from brute_forcing.check_routes import check_route


def extract_routes(dir_list, base_url):
    # Get the number of CPU available
    cpu_count = multiprocessing.cpu_count()

    # Opening the file and reading its lines
    with open(dir_list, 'rb') as file:
        lines = file.readlines()

    # Creating a ThreadPoolExecutor with max_workers set to CPU count
        with ThreadPoolExecutor(max_workers=cpu_count) as executor:
            """
            List to store futures( result of an asynchronous 
            or parallel operation that is either currently running or has already been completed.)
            for each batch of tasks
            """
            futures = []
            # Defining the batch_size to process
            batch_size = 10

            # Iterating through lines in batches
            for i in range(0, len(lines), batch_size):
                # Extracting a batch of lines
                batch = lines[i:i + batch_size]
                batch_futures = []

                for line in batch:
                    # Decoding line and removing trailing whitespaces
                    word = line.decode('utf-8').strip()
                    print(f"Checking path: /{word}")
                    # Submitting task to executor
                    batch_futures.append(executor.submit(check_route, base_url, word))

                # Adding batch futures to the list of all futures
                futures.append(batch_futures)

            for batch_futures in futures:
                # Iterating through futures in the current batch as they complete
                for future in concurrent.futures.as_completed(batch_futures):
                    # Getting the result of the completed future
                    result = future.result()
                    if result:
                        print(f"{result}: exists")
