from subdags.subdag_parallel_dag import subdag_parallel_dag_func
from os import linesep
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}
with DAG('parallel_dag',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False) as dag:

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )

    # processing_tasks is a group id
    with TaskGroup('processing_tasks') as processing_tasks:
        task_2 = BashOperator(
            task_id='task_2',
            bash_command='sleep 3'
        )
        with TaskGroup('spark_task') as spark_task:
            task3_spark = BashOperator(
                task_id='task3_spark',
                bash_command='sleep 3'
            )

        with TaskGroup('flink_task') as flink_task:
            task3_flink = BashOperator(
                task_id='task3_flink',
                bash_command='sleep 3'
            )

    # processing = SubDagOperator(
    #     task_id='processing',
    #     subdag=subdag_parallel_dag_func(
    #         'parallel_dag', 'processing', default_args)
    # )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='sleep 3'
    )

    task_1 >> processing_tasks >> task_4
