# Create your first data pipeline

### Going to create 5 tasks: 

- Creating table
- is_api_available
- extracting user
- processing user
- storing user

Note: Each time you add one task to your data pipeline, you have to do "test your task" by doing:
`airflow tasks test user_processing(dag id) creating_table(task id) 2020-01-01(date)`


1. Creating table
- create folder 'dags -> user_processing.py'
- in 'user_processing.py' file, define tasks, create table
- run webserver and scheduler
- in webserver, add connection (form). Then your database will be shown at the webUI.
- test your task

2. is_api_available
We want to make sure that the api, from where we are going to fetch the users, is available.
For this, we are going to use HTTP Sensor.
Sensor is going to wait for the API to be available before moving to the next task.
- write task in 'user_processing.py'
- run webserver and scheduler (if not running already)
- create new connection (from webUI). 
- test your task

3. Extracting users
- write task 'extracting_user'
- test your task
You will get a json of user

4. Processing user
### xcom
It is a way to share data between your tasks in airflow. For eg: getting 'user' from 'extracting_user' task and sharing that 'user' to 'processing_user' task. Read notes to see the structure.
- create task
- define function

5. Storing user into database
We will use 'bash operator'
- create a task.

We have successfully created a DAG. But right now, we dont have any dependency (no specific order).
We do this by using ">>"


Now its time, to test your complete data pipeline. Its very simple. Toggle DAG on web UI.

### DAG scheduling
What if you want to group tasks together or run tasks with some duration. This is called as DAG scheduling.

## Running tasks in parallel

*How to check the default configurations (sequential or parallel)*
`airflow config get-value core sql_alchemy_conn`
For checking executor:
`airflow config get-value core executor`

**Change configurations (in airflow.cfg) to run tasks in parallel**
1. sql_alchemy_conn = postgres+psycopg2://postgres:postgres@localhost/postgres
2. executor = LocalExecutor

Then, do these steps to set up postgresql database:
1. airflow db init (initialize database)
2. create user
`airflow users create -u admin -p admin -r Admin -f admin -l admin -e admin@airflow.com`

### Running + Scaling infinite tasks
We need multiple executors (instead of only one executor) in order to run infinite tasks in parallel. We have two executors to achieve this:
1. Celery Executor
2. Kubernetes Executor