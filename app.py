from flask import Flask, request, render_template
import requests

app = Flask(__name__)

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'  # Replace with your actual access token

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        username = request.form['handle']
        data = fetch_instagram_data(username)
    return render_template('index.html', data=data)

def fetch_instagram_data(username):
    # Step 1: Lookup user ID by username
    user_search_url = f"https://graph.facebook.com/v22.0/ig_username?username={username}&access_token={ACCESS_TOKEN}"
    user_res = requests.get(user_search_url).json()
    print(user_res)
    user_id = user_res.get('id')
    if not user_id:
        return {"error": "User not found or token invalid."}

    insights = {}

    # Step 2: Get basic user profile info
    profile_url = f"https://graph.facebook.com/v22.0/{user_id}?fields=name,username,followers_count,follows_count,media_count,profile_picture_url,biography&access_token={ACCESS_TOKEN}"
    insights['profile'] = requests.get(profile_url).json()

    # Step 3: Get account insights
    account_insights_url = f"https://graph.facebook.com/v22.0/{user_id}/insights"
    metrics = [
        "impressions", "reach", "profile_views", "website_clicks",
        "email_contacts", "phone_call_clicks", "text_message_clicks",
        "get_directions_clicks", "audience_country", "audience_gender_age",
        "audience_locale", "online_followers", "follower_count"
    ]
    insights['account_insights'] = requests.get(
        account_insights_url,
        params={
            'metric': ','.join(metrics),
            'period': 'day',
            'access_token': ACCESS_TOKEN
        }
    ).json()

    # Step 4: Get media list
    media_list_url = f"https://graph.facebook.com/v22.0/{user_id}/media"
    media_list = requests.get(media_list_url, params={
        'fields': 'id,caption,media_type,media_url,timestamp,permalink',
        'access_token': ACCESS_TOKEN
    }).json()
    insights['media'] = media_list.get('data', [])

    # Step 5: For each media item, get insights
    media_insights = []
    for media in insights['media'][:5]:  # Limit to first 5 items
        media_id = media['id']
        media_type = media['media_type']

        if media_type == 'VIDEO':
            metric_list = "impressions,reach,engagement,saved,likes,comments,video_views,video_avg_time_watched"
        elif media_type == 'REEL':
            metric_list = "plays,reach,saved,shares,total_interactions,likes,comments"
        elif media_type == 'STORY':
            metric_list = "exits,replies,taps_forward,taps_back,impressions,reach"
        else:
            metric_list = "impressions,reach,engagement,saved,likes,comments"

        media_insight_url = f"https://graph.facebook.com/v22.0/{media_id}/insights"
        media_insight = requests.get(media_insight_url, params={
            'metric': metric_list,
            'access_token': ACCESS_TOKEN
        }).json()

        media_insights.append({
            'media': media,
            'insights': media_insight.get('data', [])
        })

    insights['media_insights'] = media_insights

    return insights

if __name__ == '__main__':
    app.run(debug=True)
