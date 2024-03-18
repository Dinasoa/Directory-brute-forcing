import requests
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from brute_forcing.check_routes import check_route
import multiprocessing
import math


def extract_routes(dir_list, base_url):
    """
       Here we are going to check available paths for the given website in a multithread based on our core cpu
       and wordlist size
       :param dir_list: wordlist path
       :param base_url: the target website
    """
    # Get the number of CPU available
    cpu_count = multiprocessing.cpu_count()

    # Opening the file and reading its lines
    with open(dir_list, 'rb') as file:
        lines = file.readlines()

    total_words = len(lines)
    # Calculate batch size for each thread based on length of the wordlist and number of cpu
    batch_size = compute_batch_size(total_words, cpu_count)
    print(batch_size)

    # Creating a ThreadPoolExecutor with max_workers set to CPU count
    with ThreadPoolExecutor(max_workers=cpu_count) as executor:
        """
           List to store futures(result of parallel operation that is either 
           currently running or has already been completed.)
           for each batch of tasks
        """
        futures = []

        for i in range(0, total_words, batch_size):
            # Extracting a batch of lines
            batch = lines[i:i + batch_size]
            batch_futures = []

            for line in batch:
                word = format_line(line)
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
                    print(result)


def compute_batch_size(wordlist_size, cpu_count):
    """
           Here we are going to compute the appropriate batch size based on wordlist size and the number of cpu
           :param wordlist_size: wordlist's length
           :param cpu_count: number of cpu
           :return: number of batch size
    """
    return math.ceil(wordlist_size / cpu_count)


def format_line(line):
    """
          Here we are going to decode line in utf-8 and remove trailing whitespaces
          :param line: line to decode
          :return: line decoded
    """
    return line.decode('utf-8').strip()
