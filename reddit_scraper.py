import praw
import os


REDDIT_CLIENT_ID = ""
REDDIT_CLIENT_SECRET = ""
REDDIT_USER_AGENT = ""


USERNAME = "kojied"


os.makedirs("output", exist_ok=True)

# 🔌 Connect to Reddit
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

user = reddit.redditor(USERNAME)


print(f"\n Fetching posts by u/{USERNAME}...")
with open(f"output/{USERNAME}_posts.txt", "w", encoding="utf-8") as post_file:
    for post in user.submissions.new(limit=100):
        post_file.write(f"Title: {post.title}\n")
        post_file.write(f"Text: {post.selftext}\n")
        post_file.write(f"URL: {post.url}\n")
        post_file.write("="*60 + "\n")
print(" Posts saved.")


print(f" Fetching comments by u/{USERNAME}...")
with open(f"output/{USERNAME}_comments.txt", "w", encoding="utf-8") as comment_file:
    for comment in user.comments.new(limit=100):
        comment_file.write(f"Comment: {comment.body}\n")
        comment_file.write("="*60 + "\n")
print(" Comments saved.")

print("\n Done! All data saved in 'output/' folder.")
