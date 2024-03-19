# Directory Brute Forcing Script

## About me

- Name : ANDRIATSITOHAINA Ny Ando Mayah
- Email: hei.mayah.3@gmail.com
- ID: STD21039

## Overview

This Python script is designed for directory brute forcing, a technique used to discover hidden directories or files on a web server. The script takes a list of potential directory or file names (commonly known as a wordlist) and sends HTTP requests to the server for each item in the list. If the server responds with specific HTTP status codes (200, 500, or 403), the directory or file is considered found and added to the list of discovered items.

## What is Directory Brute Forcing?

Directory brute forcing is a method used to identify hidden or unlinked directories or files on a web server. It involves systematically testing a large number of directory or file names in an attempt to access resources that may not be publicly visible or linked from other pages. This technique is often used by security professionals to assess the security posture of a web application or by attackers seeking to discover sensitive information or potential vulnerabilities.

## How the Code Works

### Dependencies

This script requires the `requests` library, which is used to send HTTP requests to the server and handle responses.

### Functionality

1. The script reads a wordlist file containing a list of directory or file names to be tested against the target server.

2. It splits the wordlist into several parts, depending on the number of threads specified (default is 10). Each part is processed concurrently by a separate thread.

3. For each directory or file name in the wordlist part, the script constructs a URL by combining the server URL with the directory or file name.

4. It sends an HTTP GET request to the server for each URL constructed.

5. If the server responds with HTTP status codes 200, 500, or 403, the directory or file is considered found and added to the list of discovered items.

6. Once all threads have finished processing, the script prints the list of found directories or files.

## How to Test the Code

To test the script, follow these steps:

1. Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/).

2. Install the `requests` library if you haven't already by running the following command:

```python
pip install requests
```


3. Download the `script.py` file and prepare a wordlist file containing a list of directory or file names to test.

4. Open a terminal or command prompt and navigate to the directory containing `script.py` and the wordlist file.

5. Run the script with the following command:

```python
python script.py --server http://example.com --dict wordlist.txt
```
Replace `http://example.com` with the URL of the server you want to test against, and `wordlist.txt` with the filename of your wordlist.

6. The script will start testing directories against the specified server URL. Once finished, it will print the list of found directories or files.

## Disclaimer

This script is intended for educational and ethical purposes only. Do not use this script for unauthorized or malicious activities. Always ensure you have proper authorization before testing or assessing the security of any web application or server.
