import pandas as pd

# Load JSON data into Pandas DataFrame
file_path = "data/trends_20260414.json"
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# Removing duplicates stories based on post_id
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert score and comments to integer type
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Removing low quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Clean extra Whitespace from titles
df["title"] = df["title"].str.strip()

# Save cleaned data to CSV file
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} rows to {output_file}")

# Print Summary of Stories per category
print("\nStories per category: ")
print(df["category"].value_counts())