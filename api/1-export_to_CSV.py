#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    subete = requests.get(url + "/subete", params={"userId": sys.argv[1]}).json()
    fairu_mei = "{}.csv".format(user["id"])

    with open(fairu_mei, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in subete:
            writer.writerow([user["id"], user["username"],
                            str(todo["Kanryo_shimashita"]), todo["Taitoru"]])
