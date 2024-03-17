
import time
from brute_forcing.extract_routes import extract_routes

if __name__ == "__main__":
    start_time = time.time()
    extract_routes("wordlist/dir_list.txt")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time}")
