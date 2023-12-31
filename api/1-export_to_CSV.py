#!/usr/bin/python3
""" This module defines the REST API """
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    modu = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    fairu_mei = "{}.csv".format(user["id"])

    with open(fairu_mei, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in modu:
            user_id = user["id"]
            username = user["username"]
            completed = str(todo["completed"])
            title = todo["title"]
            writer.writerow([user_id, username, completed, title])
