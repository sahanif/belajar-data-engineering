from airflow.utils.dates import days_ago
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from pprint import pprint
import pandas as pd


args = {
    'owner': 'Airflow',
    'start_date': days_ago(0, hour=1, minute=0),
}

dag = DAG(
    dag_id='example_web_scrape',
    default_args=args,
    schedule_interval="0 * * * *",
    tags=['example'],
    catchup=False
)

def web_scrape():
    # Webpage url                                                                                                               
    url = 'https://id.wikipedia.org/wiki/Daftar_orang_terkaya_di_Indonesia'

    # Extract tables
    dfs = pd.read_html(url)

    # Get 7ht table                                                                                                           
    df = dfs[7]

    # Write to csv
    df.to_csv('list_orang_terkaya_di_indonesia.csv')

get_web_scrape = PythonOperator(
    task_id='get_web_scrape',
    python_callable=web_scrape,
    dag=dag,
)


def print_context(ds, **kwargs):
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

cetak_context = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)

send_email = EmailOperator(
        task_id='send_email',
        to='fia.digitalskola@gmail.com',
        subject='Faisal_DigitalSkola_Airflow',
        html_content=""" <h3>PR-3 dari Faisal</h3> """,
        files=['list_orang_terkaya_di_indonesia.csv'],
        dag=dag
)


get_web_scrape
cetak_context >> send_email
