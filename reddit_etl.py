from datetime import datetime
import praw
import re
from textblob import TextBlob
import pandas as pd

def reddit_etl(username):
    # Initialize Reddit connection
    reddit = praw.Reddit(
        client_id='ivkGswqw9R9Miz6Gax_A3w',
        client_secret='TznROcIJDr7cgr1R7lqvOF1Q4kB9fg',
        user_agent='etl_practice_project by u/Average_Enthusiast_2',
        username='Average_Enthusiast_2',
        password='Shinae@2013'
    )

    def clean_text(text):
        text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
        text = re.sub(r'\s+', ' ', text).strip()    # Remove extra spaces
        text = re.sub(r'([?.!,]){2,}', r'\1', text) # Remove repeating punctuation
        return text.strip()

    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity

    try:
        redditor = reddit.redditor(username)
        posts_data = []
        
        for post in redditor.submissions.new(limit=50):
            cleaned_title = clean_text(post.title)
            sentiment_score = get_sentiment(cleaned_title)
            post_date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            
            posts_data.append({
                'title': cleaned_title,
                'upvotes': post.score,
                'num_comments': post.num_comments,
                'created_at': post_date,
                'url': post.url,
                'sentiment_score': sentiment_score
            })
            
        df = pd.DataFrame(posts_data)
        
        # Save DataFrame to CSV
        output_path = f'/Users/harshith/Desktop/{username}_posts.csv'
        df.to_csv(output_path, index=False)
        return f"Data saved to {output_path}"
        
    except Exception as e:
        raise Exception(f"Error fetching data: {e}")

if __name__ == "__main__":
    username = input("Enter the Reddit username: ")
    reddit_etl(username)