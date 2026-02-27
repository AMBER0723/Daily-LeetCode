import os
import tweepy

# 1. Setup X API v2
client = tweepy.Client(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

# 2. Identify the latest problem solved
# We look for folders, excluding hidden ones like .github or .git
folders = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]

if not folders:
    problem_name = "a tough challenge"
else:
    # Get the folder that was updated most recently
    problem_name = max(folders, key=os.path.getmtime)

# 3. Calculate Streak
# You've done 55 days. If this is a new repo, we add your 55 to the folder count.
current_streak = 55 + len(folders)

# 4. Format the Tweet
tweet_content = (
    f"🔥 Day {current_streak} of my #LeetCode journey!\n\n"
    f"✅ Solved: {problem_name}\n"
    f"💻 Language: C++\n\n"
    f"Continuing the grind! 🚀 #BuildInPublic #Coding #Cpp"
)

# 5. Post
try:
    client.create_tweet(text=tweet_content)
    print(f"Successfully posted: {problem_name}")
except Exception as e:
    print(f"Error posting to X: {e}")
