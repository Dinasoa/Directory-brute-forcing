import requests
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from brute_forcing.check_routes import check_route
import multiprocessing
import math


def extract_routes(dir_list, base_url):
    # Get the number of CPU available
    cpu_count = multiprocessing.cpu_count()

    # Opening the file and reading its lines
    with open(dir_list, 'rb') as file:
        lines = file.readlines()

    # Calculate batch size for each thread based on length of the wordlist and number of cpu
    total_words = len(lines)
    batch_size_per_thread = math.ceil(total_words / cpu_count)

    # Creating a ThreadPoolExecutor with max_workers set to CPU count
    with ThreadPoolExecutor(max_workers=cpu_count) as executor:
        """
           List to store futures( result of parallel operation that is either 
           currently running or has already been completed.)
           for each batch of tasks
        """
        futures = []

        # Iterating through lines in batches
        for i in range(0, total_words, batch_size_per_thread):
            # Extracting a batch of lines
            batch = lines[i:i + batch_size_per_thread]
            batch_futures = []

            for line in batch:
                # Decoding line and removing trailing whitespaces
                word = line.decode('utf-8').strip()
                print(f"Checking path: /{word}")
                # Submitting task to executor
                batch_futures.append(executor.submit(check_route, base_url, word))

            futures.append(batch_futures)

        for batch_futures in futures:
            # Iterating through futures in the current batch as they complete
            for future in concurrent.futures.as_completed(batch_futures):
                # Getting the result of the completed future
                result = future.result()
                if result:
                    print(f"{result}: exists")
