#!/usr/bin/python3
""" Using request, parse response, convert to CSV """


import requests
import csv


def fetch_and_print_posts():
    """ Fetch JSONPlaceholder posts, print response status, post titles """
    rep = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", rep.status_code)

    if rep.status_code == 200:
        data = rep.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """ Fetch JSONPlaceholder posts, save selected fields, posts.csv"""
    rep = requests.get("https://jsonplaceholder.typicode.com/posts")
    if rep.status_code == 200:
        data = rep.json()
        rows = []
        for post in data:
            rows.append({"id": post["id"], "title": post["title"],
                         "body": post["body"]})
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
