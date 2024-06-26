#!/usr/bin/env python3
"""Module to fetches all post from JSONPlaceholder API."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch and print all post \
from JSONPlaceholder"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch and save all post from \
JSONPlaceholder and save to file."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()        
        for post in posts:
            data = [{"id" : post["id"], "title" : post["title"], "body" : post["body"]}]
        with open("posts.csv", "w", newline="") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
