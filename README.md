# 🤖 Reddit User Analytics ETL Pipeline

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=F73F06&width=435&lines=Reddit+Data+Pipeline;Automated+ETL+Process;Sentiment+Analysis" alt="Project Banner" />
</p>

An automated ETL (Extract, Transform, Load) pipeline that extracts Reddit user data, performs sentiment analysis, and stores the processed data using Apache Airflow for orchestration.

## 🎯 Features

- 📊 Extracts user posts data using Reddit's PRAW API
- 🧹 Implements text cleaning and normalization
- 💡 Performs sentiment analysis on post titles
- 🔄 Automated daily data collection
- 📈 Processes up to 50 most recent posts per user

## 🏗️ Architecture

```
Reddit API → PRAW → Text Processing → Sentiment Analysis → CSV Storage
     ↑______________ Airflow DAG Orchestration ______________↑
```

## 🛠️ Technologies Used

- **Apache Airflow**: Workflow orchestration
- **PRAW**: Reddit API wrapper
- **TextBlob**: Sentiment analysis
- **Pandas**: Data manipulation
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8+
- Apache Airflow
- Reddit API credentials
- Required Python packages:
  - praw
  - textblob
  - pandas

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/reddit-etl-pipeline.git
cd reddit-etl-pipeline
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Reddit API credentials**
Update `reddit_etl.py` with your Reddit API credentials:
```python
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='your_user_agent',
    username='your_username',
    password='your_password'
)
```

4. **Set up Airflow DAG**
- Copy `reddit_etl_dag.py` to your Airflow DAGs folder
- Update the target username in the DAG file
- Start Airflow webserver and scheduler

## 🔧 Configuration

### DAG Settings
- Schedule: Daily
- Retries: 1
- Retry Delay: 5 minutes

### ETL Process
- Post Limit: 50 most recent posts
- Data Cleaned: Non-ASCII characters, extra spaces, repeating punctuation
- Sentiment Analysis: TextBlob polarity score

## 📊 Output Data Format

The pipeline generates a CSV file with the following columns:
- `title`: Cleaned post title
- `upvotes`: Number of upvotes
- `num_comments`: Number of comments
- `created_at`: Post creation timestamp
- `url`: Post URL
- `sentiment_score`: Title sentiment polarity (-1 to 1)

## 🚨 Error Handling

- Non-ASCII character removal
- Proper exception handling for API failures
- Airflow retry mechanism for failed tasks

## 📝 Usage Example

**Running the ETL script directly:**
```python
python reddit_etl.py
# Enter the Reddit username when prompted
```

**Monitoring in Airflow:**
1. Access Airflow UI (default: localhost:8080)
2. Navigate to DAGs
3. Enable 'reddit_etl_dag'
4. Monitor execution

## 📫 Contact

- LinkedIn: [Harshith Keeni](https://www.linkedin.com/in/harshith-keeni)
- Email: keeniharshith@gmail.com

---

<p align="center">
  <i>Built with ❤️ by Harshith Keeni</i>
</p>
