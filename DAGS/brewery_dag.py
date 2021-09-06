from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import brewery_pipeline

default_args = {
    'owner': 'Nikki',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5)
}

with DAG (
    'brewery_pipeline',
    default_args=default_args,
    description='brewery_pipeline',
    schedule_interval=timedelta(days=7),
    start_date=days_ago(1)
) as dag:
    
    # first task, load in the data
    t1 = PythonOperator(
        task_id = 'load_data'
        python_callable=loadData('https://api.openbrewerydb.org/breweries')
    )

    # second task, organize data by given city, state
    t2 = PythonOperator(
        task_id = 'by_city_state'
        python_callable=breweryLocation('Newark', 'Delaware')
    )

    # set the dependencies
    t1 >> t2