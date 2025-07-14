import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_user_data(username, max_items=100):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for submission in user.submissions.new(limit=max_items):
        posts.append({
            "type": "post",
            "title": submission.title,
            "body": submission.selftext,
            "url": submission.url,
            "permalink": f"https://www.reddit.com{submission.permalink}"
        })

    for comment in user.comments.new(limit=max_items):
        comments.append({
            "type": "comment",
            "body": comment.body,
            "permalink": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments
