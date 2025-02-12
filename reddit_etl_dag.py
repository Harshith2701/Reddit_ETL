from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from reddit_etl import reddit_etl

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False,
    'email_on_failure': False,
}

# Function to pass username parameter
def process_reddit_user(username):
    return reddit_etl(username)

with DAG(
    'reddit_etl_dag',
    default_args=default_args,
    description='Reddit ETL pipeline',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
) as dag:

    extract_reddit_data = PythonOperator(
        task_id='extract_reddit_data',
        python_callable=process_reddit_user,
        op_kwargs={'username': 'Python'},  # Replace with target username
    )