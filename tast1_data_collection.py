import json
from datetime import datetime
import os
import time
import requests
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
try:
    # Fetch top story ID's from HackerNews API
    response = requests.get(url)
    story_ids = response.json()[:500]
except:
    print("Failed to fetch top stories")
    story_ids = []

# Function to assign category based on keywords in title
def get_category(title):
    title = title.lower()

    if "ai" in title or "software" in title or "tech" in title or "code" in title or "computer" in title or "data" in title or "cloud" in title or "api" in title or "gpu" in title or "llm" in title:
        return "Technology"
    elif "war" in title or "government" in title or "country" in title or "president" in title or "election" in title or "climate" in title or "attack" in title or "global" in title:
        return "Worldnews"
    elif "nfl" in title or "nba" in title or "fifa" in title or "sport" in title or "game" in title or "team" in title or "player" in title or "league" in title or "championship" in title:
        return "Sports"
    elif "research" in title or "study" in title or "space" in title or "physics" in title or "biology" in title or "discovery" in title or "nasa" in title or "genome" in title:
        return "Science"
    elif "movie" in title or "film" in title or "music" in title or "netflix" in title or "game" in title or "book" in title or "show" in title or "award" in title or "streaming" in title:
        return "Entertainment"
    else:
        return "Others"

category_count = {
    "Technology" : 0,
    "Worldnews" : 0,
    "Sports" : 0,
    "Science" : 0,
    "Entertainment" : 0,
    "Others" : 0
}

all_data = []

# Loop through story ID's and fetch details
for story_id in story_ids:
    try:
        res = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
        story = res.json()
    except:
        print(f"Failed to fetch story {story_id}") # Handle request failure
        continue
    
    # Skip invalid or missing data
    if not story or story.get("title") is None:
        continue

    category = get_category(story["title"])
    
    if category_count[category] < 25:
        data = {
            "post_id" : story.get("id"),
            "title" : story.get("title"),
            "category" : category,
            "score" : story.get("score", 0),
            "num_comments" : story.get("descendants", 0),
            "author" : story.get("by", "unknown"),
            "collected_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        all_data.append(data)
        category_count[category]+=1
    
        if category_count[category] == 25:
            print(f"{category} completed. Waiting 2 seconds...")
            time.sleep(2)
    
    # Assign category and limit to 25 per category
    if all(count>=25 for count in category_count.values()):
        break

# Create data folder if not exists and save results to JSON file
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)

print(f"Collected {len(all_data)} stories. Saved to {filename}")