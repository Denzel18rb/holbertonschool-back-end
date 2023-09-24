#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    Benotzer = requests.get(url + "/users").json()
    subete_modu = {}

    for user in Benotzer:
        yuza_id = user['id']
        modu = requests.get(url + "/todos", params={"userId": yuza_id}).json()
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in modu]
        subete_modu[yuza_id] = user_todos

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(subete_modu, outfile)
