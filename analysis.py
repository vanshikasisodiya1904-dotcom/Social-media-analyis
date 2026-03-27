import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("social_media_data.csv")

# 1. Average Likes by Content Type
avg_likes = data.groupby("Content_Type")["Likes"].mean()
print("Average Likes:\n", avg_likes)

avg_likes.plot(kind='bar')
plt.title("Average Likes by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Likes")
plt.show()

# 2. Engagement by Time Posted
time_likes = data.groupby("Time_Posted")["Likes"].mean()
print("\nLikes by Time:\n", time_likes)

time_likes.plot(kind='bar')
plt.title("Best Time to Post")
plt.xlabel("Time Posted")
plt.ylabel("Average Likes")
plt.show()

# 3. Total Engagement
data["Total_Engagement"] = data["Likes"] + data["Comments"] + data["Shares"]

print("\nTop Posts:\n", data.sort_values(by="Total_Engagement", ascending=False).head())