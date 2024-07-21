from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 7, 20),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "web_scraping_dag",
    default_args=default_args,
    description="A DAG to automate web scraping with Scrapy",
    schedule_interval="0 */10 * * *",  # Schedule to run every 10 minutes
    template_searchpath=["/home/nyagah/Code/personal/apartment-price-predictor"],
)

# scrape_command = "scrapy crawl buyrentkenya"
scrape_command = "cd /home/nyagah/Code/personal/apartment-price-predictor && poetry run scrapy crawl buyrentkenya"

scrape_task = BashOperator(
    task_id="scrape_data",
    bash_command=scrape_command,
    dag=dag,
)
