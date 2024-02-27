import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 3, 10, tz="Asia/Seoul"),
    catchup=True,
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint #예쁘게 출력해주는 print
        pprint(kwargs)

    show_templates()
    
