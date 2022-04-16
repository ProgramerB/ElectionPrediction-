import praw
import re
import wallet
import ElectionLib
import demoji

def clean(text):
    text=demoji.replace_with_desc(text)
    text = text.lower()
    return re.sub('(https:\/\/.*[\r\n]*)','',text)

def fetch():

    cl_id,cl_sc,ua = wallet.redditKeys()
    reddit=praw.Reddit(
    client_id=cl_id,
    client_secret=cl_sc,
    user_agent=ua)

    bjp_keywords=['BJP','Bharatiya Janata Party','Narendra Modi','Modi']
    inc_keywords=['Indian National Congress','Rahul Gandhi','Sonia Gandhi','Manmohan Singh']

    num = int(input("Enter number of tweets:"))
    num = num / 2

    for key in bjp_keywords:
        sub=reddit.subreddit('all').search(key,limit=num)#IndiaSpeaks,indianews
        #hot_sub=sub.hot(limit=10)

        #for post in hot_sub:
        for post in sub:
            selftext=clean(post.selftext)
            print(selftext)
            title = clean(post.title)
            ElectionLib.importDataReddit(post.id, title, selftext, post.created_utc, post.score,'b',key)
        
    for key in inc_keywords:
        sub=reddit.subreddit('all').search(key,limit=num)#IndiaSpeaks,indianews
        #hot_sub=sub.hot(limit=10)

        #for post in hot_sub:
        for post in sub:
            selftext=clean(post.selftext)
            print(selftext)
            title = clean(post.title)
            ElectionLib.importDataReddit(post.id, title, selftext, post.created_utc, post.score,'i',key)

fetch()