# ig-follower-insights

A Python tool that analyzes your Instagram data export to reveal follower relationships—see who you follow but doesn’t follow back, and who follows you but you don’t follow back.

---

## Features

- **Find who you follow that doesn’t follow you back**
- **Find who follows you that you don’t follow back**
- **Clean, intuitive output**
- **Works entirely offline for your privacy**

---

## Getting Started

### 1. Export Your Instagram Data

1. Go to the [Meta Accounts Center](https://accountscenter.meta.com/).
2. Navigate to the **"Your information and permissions"** tab.
3. Click the **"Download your information"** button.
4. In the export options:
    - Under the **"Connections"** section, select **"Followers and following"**.
    - Choose **JSON** as the file format.
    - Set the time frame to **All time**.
5. Complete the request and wait for an email from Meta with your download link.
6. Download your data and **extract the ZIP file**. Find the `connections` folder (it contains your `followers.json` and `following.json` files).

---

### 2. Prepare Your Workspace

- Place the entire `connections` folder in the **same directory** as this Python script.
- Ensure you have Python 3 installed.

---

### 3. Run the Script

```python ig_follower_insights.py```


- The script will process your data and output results to a new folder called `output` in the same directory.

---

## Output

- Results are saved as text files in the `output` folder:
    - `not_following_back.txt`: People who follow you, but you don’t follow back.
    - `not_followed_back.txt`: People you follow, but who don’t follow you back.

---

## Privacy

This tool runs **entirely offline**. Your Instagram data never leaves your computer.

---