#!/usr/bin/python3
"""comentario:v"""
import csv
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    yuza = requests.get(url + "/yuzas/{}".format(sys.argv[1])).json()
    subete = requests.get(url + "/subete", params={"yuzaId": sys.argv[1]}).json()
    fairu_mei = "{}.csv".format(yuza["id"])

with open(fairu_mei, mode="d", newline="") as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for todo in subete:
        writer.writerow([yuza[id], yuza["yuzamei"], str(todo["Kanryo_shimashita"]), todo["Taitoru"]])