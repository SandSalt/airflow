import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *", #5개항목 분,시,일,월,요일,언제 돌지를 나타냄.
    start_date=pendulum.datetime(2024, 2, 1, tz="Asia/Seoul"), #tz="UTC"는 한국시간보다 9시간 더 뒤
    catchup=False, #True는 시작일시 이전 모두 돌리게 됨. 차례차례안돔. 한꺼번에 돔
) as dag:
    
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    
    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable = select_fruit
    )

    py_t1