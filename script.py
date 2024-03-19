import argparse
import requests
import threading
import time

directory_list = []

# This function test the server url with different endpoints contained in wordlist_part
def test_directories(url, wordlist_part):
    for directory in wordlist_part:
        endpoint_url = url + "/" + directory
        print("Testing this request : " + endpoint_url)
        response = requests.get(endpoint_url)
        if response.status_code in [200, 500, 403]:
            directory_list.append(endpoint_url)
    return directory_list

def main():
    parser = argparse.ArgumentParser(description="Brute force directory enumeration script")
    parser.add_argument("--server", required=True, help="Server URL to test directories against")
    parser.add_argument("--dict", required=True, help="Path to the dictionary file containing directory names")
    args = parser.parse_args()

    url = args.server
    wordlist_path = args.dict

    # Open the word list txt file and read the contents
    with open(wordlist_path, "r") as f:
        wordlist = f.read().splitlines()

    # Splitting the word list into 10 parts => 300 / 10 = 30
    wordlist_length = len(wordlist)
    part_length = wordlist_length // 10

    # Initiate threading
    threads = []

    for i in range(10):
        start_index = i * part_length
        end_index = (i + 1) * part_length if i < 9 else wordlist_length
        wordlist_part = wordlist[start_index:end_index]
        thread = threading.Thread(target=test_directories, args=(url, wordlist_part))
        threads.append(thread)
        thread.start()

    # Waiting for all threads to end
    for thread in threads:
        thread.join()

    # Printing found directories
    print("-----------------------------------------------------------------")
    print("AVAILABLE DIRECTORIES")
    print("-----------------------------------------------------------------")

    for available_directory in directory_list:
        print("Available directory found : ", available_directory)

if __name__ == "__main__":
    main()
