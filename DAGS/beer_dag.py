from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from beerDatabase import *

default_args = {
    'owner': 'Nikki',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5)
}

with DAG (
    'beerDatabase',
    default_args=default_args,
    description='beer_pipeline',
    schedule_interval=timedelta(days=7),
    start_date=days_ago(1)
) as dag:
    
    # first task, load in the data and organizes
    t1 = PythonOperator(
        task_id='load_data',
        python_callable=beerDatabase
    )

    # each of the tasks below represents each of the different profile flavors
    t2 = PythonOperator(
        task_id='crisp',
        python_callable=crisp
    )

    t3 = PythonOperator(
        task_id='hoppy',
        python_callable=hoppy
    )

    t4 = PythonOperator(
        task_id='malty',
        python_callable=malty
    )

    t5 = PythonOperator(
        task_id='dark',
        python_callable=dark
    )

    t6 = PythonOperator(
        task_id='smoke',
        python_callable=smoke
    )

    t7 = PythonOperator(
        task_id='fruity',
        python_callable=fruity
    )

    t8 = PythonOperator(
        task_id='sour',
        python_callable=sour
    )

    t9 = PythonOperator(
        task_id='graph',
        python_callable=graph
    )

    # set the dependencies
    t1 >> [t2, t3, t4, t5, t6, t7, t8] >> t9