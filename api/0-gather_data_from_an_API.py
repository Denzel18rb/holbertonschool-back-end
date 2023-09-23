#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    Tasuku_no_gokei = len(todos)
    Kanryo_shita_tasuku = sum(1 for todo in todos if todo["completed"])

    print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), Kanryo_shita_tasuku, Tasuku_no_gokei))

    [print(f"\t {todo['title']}") for todo in todos if todo["completed"]]
