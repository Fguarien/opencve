from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

with DAG(
    dag_id='test_smtp_from_email',
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    email_task = EmailOperator(
        task_id='send_email',
        conn_id='smtp_test',
        to='contact@savethemall.eu',
        subject='Test Email',
        html_content='This is a test email.',
    )