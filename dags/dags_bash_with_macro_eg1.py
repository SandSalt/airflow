from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

import pendulum

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *", # 매월 말일에 실행 되는 DAG
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False    
) as dag:
    
    # Start_date : 전일 말일, END_DATE: 1일 전
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={'START_DATE': '{{ data_interval_start.in_timezone("Asia/Seoul") | ds}}',
             'END_DATE': '{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.deteutil.relativedelta.relativedelta(days=1)) | ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE : $END_DATE"'
    )