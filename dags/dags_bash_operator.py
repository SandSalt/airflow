
import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", #5개항목 분,시,일,월,요일,언제 돌지를 나타냄.
    start_date=pendulum.datetime(2024, 2, 1, tz="Asia/Seoul"), #tz="UTC"는 한국시간보다 9시간 더 뒤
    catchup=False, #True는 시작일시 이전 모두 돌리게 됨. 차례차례안돔. 한꺼번에 돔
    #dagrun_timeout=datetime.timedelta(minutes=60), #60분이상 돌면 실패처리함.
    #tags=["example", "example2"],
    params={"example_key": "example_value"}, #테스크들에 공통적으로 넘겨줄 파라미터
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami", #어떤 쉘스크립트를 실행할지.
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2