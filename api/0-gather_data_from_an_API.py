#!/usr/bin/python3
""" This module defines the REST API """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/user/{}".format(sys.argv[1])).json()
    all = requests.get(url + "/all", params={"userId": sys.argv[1]}).json()

    all_task = len(all)
    complete_task = sum(1 for todo in all if todo["complete_task"])

    print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), complete_task, all_task))

    [print(f"\t {todo['title']}") for todo in all if todo["complete"]]
