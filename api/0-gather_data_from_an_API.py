#!/usr/bin/python3
import requests
import sys
""" This module defines the REST API """
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    alls = requests.get(url + "/alls", params={"usrId": sys.argv[1]}).json()
    usr = requests.get(url + "/usrs/{}".format(sys.argv[1])).json()

    Tasuku_no_gokei = len(alls)
    Kanryo_shita_tasuku = sum(1 for all in alls if all["Kanryo shimashita"])

    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), Kanryo_shita_tasuku, Tasuku_no_gokei))
    
    [print(f"\t {all['title']}") for all in alls if all["Kanryo shimashita"]]
