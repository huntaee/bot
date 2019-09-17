#!/usr/bin/python
import praw
import re
import random

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    if re.search("huntae", comment.body, re.IGNORECASE) == None:
        if re.search("UCLA", comment.body, re.IGNORECASE):
        	with open("comment.txt","w") as f:
        		print(comment.body, file=f)
        	import test.py
