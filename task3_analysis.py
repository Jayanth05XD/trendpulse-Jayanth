import pandas as pd
import numpy as np

# Load cleaned CSV file
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

# print the first 5 rows
print("\nFirst 5 rows: ")
print(df.head())

# Print the shape of the DataFrame
print(f"Shape of the DataFrame: {df.shape}")

# Print the average score and num_comments accross all stories
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print("Average Score: ", avg_score)
print("Average Comments: ", avg_comments)

scores = df["score"].values

# Mean, Median and standard deviation of score
print("Mean of score: ", np.mean(scores))
print("Median of score: ", np.median(scores))
print("Standard Deviation of score: ", np.std(scores))

# Highest score and Lowest score
print("Highest score: ", np.min(scores))
print("Lowest score: ", np.min(scores))

# Category with most stories
category_count = df["category"].value_counts()
top_category = category_count.idxmax()
top_count = category_count.max()
print(f"Most stories in {top_category} ({top_count} stories)")

# Story with more comments
max_comments_row = df.loc[df["num_comments"].idxmax()]
print(f"Max commented story: {max_comments_row['title']} - {max_comments_row['num_comments']} comments")

# Add 2 new columns
df["engagement"] = df["num_comments"]/(df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# Save the Result
output_file = "data/trends_analysed.csv"
df.to_csv(output_file)
print(f"Saved to {output_file}")