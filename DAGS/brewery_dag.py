from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from brewDatabase import *

default_args = {
    'owner': 'Nikki',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5)
}

with DAG (
    'brewDatabase',
    default_args=default_args,
    description='brewery_pipeline',
    schedule_interval=timedelta(days=7),
    start_date=days_ago(1)
) as dag:
    
    # first task, load in the data
    t1 = PythonOperator(
        task_id='load_data',
        python_callable=loadData
    )

    # second task, organize data by given city, state
    t2 = PythonOperator(
        task_id='organize_data',
        python_callable=organizeData
    )

    t3 = PythonOperator(
        task_id='brewery_locator',
        python_callable=brewLocator
    )

    t4 = PythonOperator(
        task_id='select_another',
        python_callable=selection
    )

    # set the dependencies
    t1 >> t2 >> t3 >> t4