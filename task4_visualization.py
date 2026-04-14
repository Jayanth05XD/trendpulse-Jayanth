import pandas as pd
import matplotlib.pyplot as plt
import os

# Load analysed data
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create Outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# Chart - 1 (Horizontal bar): Top Stories by score
# Sort top 10 stories by scores
top_stories = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top_stories["short_title"] = top_stories["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top_stories["short_title"], top_stories["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# Chart - 2 (Bar) : Top Stories by category
category_counts = df["category"].value_counts()
colors = ["red", "blue", "green", "orange", "purple", "cyan"]
plt.figure()
plt.bar(category_counts.index, category_counts.values, color=colors[:len(category_counts)])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")
plt.close()

# Chart - 3 (Scatter) : Score Vs Comments
plt.figure()
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]
plt.scatter(popular["score"], popular["num_comments"], label = "Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label = "Not Popular")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score Vs Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.close()