import requests
import json

# Get your LinkedIn API credentials
# You can get these from the LinkedIn Developer Platform
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Create a session with your LinkedIn API credentials
session = requests.Session()
session.auth = (client_id, client_secret)

# Get your access token
access_token_url = "https://api.linkedin.com/v1/oauth2/accessToken"
params = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

response = session.post(access_token_url, params=params)
access_token = response.json()["access_token"]

# Upload a post
post_url = "https://api.linkedin.com/v1/posts"
params = {
    "title": "My Post Title",
    "summary": "My Post Summary",
    "content": "My Post Content",
    "visibility": "PUBLIC",
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = session.post(post_url, params=params, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Post uploaded successfully!")
else:
    print("Error uploading post:", response.status_code)
