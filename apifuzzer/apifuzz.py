'''API fuzzer module for ITHS projekt.
This module takes an api as an argument 
when running script from the cli
and tries to make a get request
from various endpoints'''

import pprint
import json
import re
import argparse
import sys
import requests

def validate_api(api) -> bool:
    '''function for validating the users api url to make sure its a valid api url'''

    pattern = re.compile(r"^https:\/\/api\.[a-zA-Z0-9-]+\.[a-z]{2,6}\/(api\/)?v[0-9]+(\/[a-zA-Z0-9\/_-]+)?\/?$")
    try:
        result = bool(pattern.match(api))
        return result
    except TypeError:
        return False
    except UnboundLocalError:
        return False

def save(filename):
    '''function for saving the result of the fuzz to a json file'''
    with open(f"{filename}.json","w", encoding="utf-8") as f:
        f.write(json.dumps(data_storage, indent=4, sort_keys=True))
        print(f"File was saved as: {filename}.json")

def verbose():
    '''function for verbose state of script '''
    pprint.pprint(data_storage)

data_storage = {}


def loop(user_api=None):
    '''function for loop that fuzzes through the endpoints provided by the list of endpoints
    and stores the data of the result using json'''
    valid = validate_api(user_api)

    if valid is True:
        pass
    else:
        print("API not valid.")
        sys.exit()

    with open("LAPIe&objects.txt", "r", encoding="utf-8") as file:
        for line in file:
            ep = line.strip()
            if not ep:
                continue

            api = f"{user_api}{ep}?format=json"

            try:
                res = requests.get(url=api, timeout=10)
                if res.status_code in (404,500):
                    continue
                print(f"endpoint: {ep}")
                print(f"status response: {res}")
                data = res.json()
                if data:
                    data_storage[ep] = data
            except requests.exceptions.JSONDecodeError:
                continue


def main():
    '''main function for script to take arguments through cli'''
    parser = argparse.ArgumentParser(description="kontrollera responser och data från olika endpoints")
    parser.add_argument("API", help="input API url")
    parser.add_argument("-v", "--verbose", action="store_true", help="Visar utökad info")
    parser.add_argument("-s", "--save", help="save the result of the fuzz to json file")

    args = parser.parse_args()

    if args.API:
        loop(args.API)
    if args.save:
        save(args.save)

    if args.verbose:
        verbose()

if __name__ == "__main__":
    main()
