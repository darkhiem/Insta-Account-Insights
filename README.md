<h1 align="center">Instagram Account Insights 📸📊</h1>

This project is a lightweight web application that allows users to fetch and view insights for any public Instagram account. It utilizes the **Instagram Graph API** and is powered by **Flask**, providing a seamless experience through a minimalistic HTML/CSS frontend.

---

## 🚀 Features

- 🔍 Fetch public Instagram account data using Graph API
- 📄 View comprehensive statistics like:
  - Profile information (name, username, bio)
  - Follower and following counts
  - Total media count
  - Profile picture
- 📈 Access detailed account insights including:
  - Impressions and reach
  - Profile views and website clicks
  - Contact button interactions
  - Audience demographics
- 📸 View media insights for recent posts with metrics like:
  - Engagement, likes, comments, saves
  - Video views (for video content)
  - Reach and impressions
- 🧠 Lightweight Flask backend with direct API integration
- 🌐 Responsive frontend using HTML & CSS

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS  
- **API**: Instagram Graph API  
- **Deployment Ready**: Minimal dependencies for quick hosting  

---

## 🗂️ Key Components

- `app.py`: Core Flask backend for routing and Instagram Graph API integration
- `templates/index.html`: Main HTML template for rendering account insights
- `static/style.css`: Styling for the web interface
- Environment setup with Graph API access token

---

## 📊 Data Processing

The application fetches and processes Instagram data in several steps:
1. User ID lookup by username
2. Basic profile information retrieval 
3. Account insights collection (metrics like impressions, reach, profile views)
4. Recent media listing with details
5. Per-post insights collection with type-specific metrics

---

## 💡 Use Cases

- 📈 Analyze any public Instagram profile's detailed metrics  
- 🕵️ Track influencer statistics for brand collaboration  
- 📊 Display real-time profile stats in dashboards  
- 🔍 Examine engagement patterns across different post types
- 🎯 Identify best-performing content by engagement

---

## ⚠️ Disclaimer

- This app uses the official Instagram Graph API with proper authentication
- Ensure you have proper authorization to access Instagram account data
- All API requests require a valid access token

---
