#!/usr/bin/python
import praw
import re
import random

quotes = \
[
    " UCLA was founded in 1919. ",
    " UCLA’s football team was also known as the “Grizzlies” at one point, but since University of Montana had prior rights to that name, UCLA changed it to “Bruins” in 1928. ",
    " UCLA’s colors are “True Blue” and gold, and were chosen specifically to represent the state’s ocean and wildflowers. ",
    " Legendary coach John Wooden won ten national championships in basketball during his tenure at UCLA. No other school has won as many championships. Kentucky is second, with eight national championships ",
    " UCLA receives the most college applications than any university in the world. Each year, it sets a new record. ",
    " UCLA’s award-winning newspaper, the Daily Bruin, is the third most circulated newspaper in Los Angeles. It has been consistently ranked as the top college newspaper in the country. ",
    " Ray Bradbury wrote his classic novel Fahrenheit 451 at Powell Library in 1951. He was looking for a quiet space outside of his home and took a liking to the Powell Library basement. ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("UCLA", comment.body, re.IGNORECASE):
            reply = "Huntae the bot says: " + random.choice(quotes)
            comment.reply(reply)
