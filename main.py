import os
from CloudManagement.AwsContainer import AwsContainer
from CloudManagement.BaseCloudShellCommand import BaseCloudShellCommand
from Workflows.WorkFlow import WorkFlow

#
# def runAirflow():
#     os.system("cd /home/kkoz34/PycharmProjects/PegasusInvoker/test_workflow/submit/kkoz34/pegasus/diamond/run0053")
#
#     from airflow import DAG
#     from airflow.operators.bash import BashOperator
#     from datetime import datetime
#
#     default_args = {
#         'owner': 'admin',
#         'start_date': datetime.now()
#     }
#
#     dag = DAG(
#         'pegasus_workflow',
#         default_args=default_args,
#     )
#
#     # Define a BashOperator to execute the Pegasus workflow using pegasus-run
#     pegasus_task = BashOperator(
#         task_id='run_pegasus_workflow',
#         bash_command='pegasus-run workflow.dag',
#         dag=dag,
#     )






if __name__ == '__main__':
    os.system("pwd")

    awsContainer = AwsContainer("/home/kkoz34/vockey2.pem",
                                                           "ubuntu@ec**********.compute-1.amazonaws.com")

    workflow = WorkFlow("/home/kkoz34/PycharmProjects/PegasusInvoker/test_workflow",
                              "generate.sh",
                              "workflow.yml", awsContainer)

    workflow.generate()
    workflow.plan()
    workflow.run()
    workflow.status_continuum()
    workflow.generate_statistics()
    workflow.transfer_file()

    paramikoInstance = BaseCloudShellCommand(awsContainer, "pwd")
    paramikoInstance.execute()







