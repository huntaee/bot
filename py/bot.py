#!/usr/bin/python
import praw
import re
import random

quotes = \
[
" I love UCLA ",
" I hate UCLA ",
" Go Bruins ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("explainlikeimfive")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("UCLA", comment.body, re.IGNORECASE):
            reply = "Huntae the bot says: " + random.choice(quotes)
            comment.reply(reply)
