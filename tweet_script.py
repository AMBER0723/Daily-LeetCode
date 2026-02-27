import os
import tweepy
import sys

# 1. Setup X API v2 (The FREE one)
try:
    client = tweepy.Client(
        consumer_key=os.environ["CONSUMER_KEY"],
        consumer_secret=os.environ["CONSUMER_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    )
except Exception as e:
    print(f"Auth Setup Error: {e}")
    sys.exit(1)

# 2. Identify folders
folders = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]

if not folders:
    problem_name = "3666. Minimum Operations to Equalize Binary String"
else:
    problem_name = max(folders, key=os.path.getmtime)

# 3. Content
current_streak = 55 + len(folders)
tweet_content = (
    f"🔥 Day {current_streak} of #LeetCode\n\n"
    f"✅ Solved: {problem_name}\n"
    f"💻 Language: C++\n\n"
    f"#BuildInPublic #Coding #Cpp"
)

# 4. Post using v2
try:
    # This specific method uses the free v2 API
    response = client.create_tweet(text=tweet_content)
    print(f"✅ Successfully posted! Tweet ID: {response.data['id']}")
except Exception as e:
    print(f"❌ X API Error: {e}")
    sys.exit(1)
