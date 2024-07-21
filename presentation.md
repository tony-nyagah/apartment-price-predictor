To set up Apache Airflow to automate the scraping process you can follow these steps:

1. **Install Apache Airflow**: If you haven't already, you can install Apache Airflow using pip:
   
   ```
   pip install apache-airflow
   ```

2. **Initialize the Airflow database**:
   
   Initialize the database that Airflow uses to store its metadata:
   
   ```
   airflow initdb
   ```

3. **Create a new DAG (Directed Acyclic Graph)**:
   
   In your Airflow installation directory, located in your home folder, navigate to the `dags` folder. Create a new Python file for your DAG, for example, `web_scraping_dag.py`.

4. **Define your DAG**:
   
   Define your DAG in the Python file. Here's an example of how you can set up a DAG to run your Scrapy spider every day at 12 am:

   ```python
   from airflow import DAG
   from airflow.operators.bash_operator import BashOperator
   from datetime import datetime
   from datetime import timedelta

   default_args = {
       'owner': 'airflow',
       'depends_on_past': False,
       'start_date': datetime(2022, 1, 1),
       'email_on_failure': False,
       'email_on_retry': False,
       'retries': 1,
       'retry_delay': timedelta(minutes=5),
   }

   dag = DAG(
       'web_scraping_dag',
       default_args=default_args,
       description='A DAG to automate web scraping with Scrapy',
       schedule_interval='0 0 * * *',  # Schedule to run every day at 12 am
   )

   scrape_command = 'scrapy crawl buyrentkenya'

   scrape_task = BashOperator(
       task_id='scrape_data',
       bash_command=scrape_command,
       dag=dag,
   )
   ```

5. **Run your DAG**:
   
   Start the Airflow web server and scheduler:
   
   ```
   airflow webserver --port 8080
   airflow scheduler
   ```

   Access the Airflow web interface at `http://localhost:8080` and enable your DAG.

6. **Monitor your DAG**:
   
   You can monitor the progress and logs of your DAG in the Airflow web interface. The DAG will run automatically every day at 12 am as per the schedule you defined.

With these steps, you should be able to set up Apache Airflow to automate the scraping process to run every day at 12 am. Make sure to adjust the DAG definition and settings according to your specific requirements.