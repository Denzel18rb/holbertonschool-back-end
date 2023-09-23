#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    yuza = requests.get(url + "/yuzas/{}".format(sys.argv[1])).json()
    subete = requests.get(url + "/subete", params={"yuzaId": sys.argv[1]}).json()

    Tasuku_no_gokei = len(subete)
    Kanryo_shita_tasuku = sum(1 for todo in subete if todo["Kanryo_shimashita"])

    print("Employee {} is done with tasks({}/{}):".format(
            yuza.get("name"), Kanryo_shita_tasuku, Tasuku_no_gokei))

    [print(f"\t {todo['Taitoru']}") for todo in subete if todo["Kanryo_shimashita"]]
