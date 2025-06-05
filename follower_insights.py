import json
import os

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Load the JSON files
with open('connections/followers_and_following/following.json') as f:
    following_data = json.load(f)

with open('connections/followers_and_following/followers_1.json') as f:
    followers_data = json.load(f)

# Extract the usernames from the following data
following_usernames = [item['string_list_data'][0]['value'] for item in following_data['relationships_following']]
following_usernames = set(following_usernames)

# Extract the usernames from the followers data
followers_usernames = [item['string_list_data'][0]['value'] for item in followers_data]
followers_usernames = set(followers_usernames)

# Find usernames I am not following back
not_following_back = followers_usernames - following_usernames

# Find usernames that are not following me back
not_followed_back = following_usernames - followers_usernames

# Function to write lists to files in an aesthetic way
def write_usernames_to_file(filename, title, usernames):
    with open(f'output/{filename}', 'w') as f:
        f.write("=" * 50 + "\n")
        f.write(f"{title} ({len(usernames)})\n")
        f.write("=" * 50 + "\n")
        if usernames:
            for i, username in enumerate(sorted(usernames), 1):
                f.write(f"{i:3}. {username}\n")
        else:
            f.write("None 🎉\n")
        f.write("-" * 50 + "\n")

# Write the results to files
write_usernames_to_file('not_following_back.txt', "People who follow you (but you don't follow back)", not_following_back)
write_usernames_to_file('not_followed_back.txt', "People you follow (but they don't follow you back)", not_followed_back)

# Also print to console for immediate feedback
print("\nResults have been written to the 'output' directory:")
print("- output/not_following_back.txt")
print("- output/not_followed_back.txt")