#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    yuza_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    modu = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    
    yuza_zenin = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in modu]
    
    Shutsuryoku_deta = {yuza_id: yuza_zenin}

    with open(f"{yuza_zenin}.json", "w") as Autofairu:
        json.dump(Shutsuryoku_deta, Autofairu)