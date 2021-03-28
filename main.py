#! python3
import os
import json
import argparse
from time import sleep
from urllib.request import (Request, urlopen, urlretrieve)
import praw
import pandas as pd
import datetime as dt

CLIENT_ID = 'iXXMGYkMSnr1iQ'
CLIENT_SECRET = 'KM3ZItCjVaawTLGz9KdT8UVdMUoacA'
USER_AGENT = 'DnD-art scraper-test'

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)
subreddit = reddit.subreddit('DnD')


def main():

    choice = input("Please enter a search criteria for your desired character/class (Elf, Rogue, Wizard, etc.)\n")

    def print_hi(name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print_hi('Fetching relevant posts...')
    search_subreddit = subreddit.search(choice, limit=10)

    for submission in search_subreddit:
        if submission.url.endswith(".png") | submission.url.endswith(".jpg"):
            print(submission.title, submission.url)
        else:
            subreddit.search(choice)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
