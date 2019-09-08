#!/usr/bin/python
import praw
import re
import random

quotes = \
[
" 1 ",
" 2 ",
"3 ",
"4 ",
" 5 ",
" 6",
"7",
"8 ",
"9 ",
" 10 ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("dataisbeautiful")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Huntae", comment.body, re.IGNORECASE):
            reply = "Huntae the says: " + random.choice(quotes)
            comment.reply(reply)
            print(reply)
