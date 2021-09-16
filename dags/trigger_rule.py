from airflow import DAG
from airflow.configuration import default_config_yaml
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('trigger_rule', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='exit 1',  # exit 0 means this task will get succeded
        do_xcom_push=False
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='exit 1',
        do_xcom_push=False
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='exit 0',
        do_xcom_push=False,
        trigger_rule='all_failed'
    )

    [task_1, task_2] >> task_3
