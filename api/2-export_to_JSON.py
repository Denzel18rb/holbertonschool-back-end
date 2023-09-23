#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    yuza_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(yuza_id)).json()
    modu = requests.get(url + "/todos", params={"userId": yuza_id}).json()

    yuza_modu = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in modu]

    Shutsuryoku_deta = {yuza_id: yuza_modu}

    with open(f"{yuza_id}.json", "w") as outfile:
        json.dump(Shutsuryoku_deta, outfile)
