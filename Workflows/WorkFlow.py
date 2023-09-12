import os
import time

from CloudManagement.DataTransfer import DataTranserService
from Commands.BaseShellCommand import BaseShellCommand
from Commands.GenerateStatisticsWorkflowCommand import GenerateStatisticsWorkflowCommand
from Commands.PlanWorkflowCommand import PlanWorkflowCommand
from Commands.RunWorkflowCommand import RunWorkflowCommand
from Commands.StatusWorkflowCommand import StatusWorkflowCommand
from Data.InvocationDataProvider import InvocationDataProvider


class WorkFlow:
    def __init__(self, working_directory, generate_script, workflow_yml, aws_container):
        os.chdir(working_directory)
        self.generateCommand = BaseShellCommand("sh " + working_directory + "/" + generate_script)
        self.planCommand = PlanWorkflowCommand(workflow_yml)
        self.runCommand = None
        self.statusCommand = None
        self.removeCommand = None
        self.workflowDirectory = "/home/kkoz34/PycharmProjects/PegasusInvoker/test_workflow/submit/kkoz34/pegasus/diamond/run0053"
        self.isWorkflowReady = False
        self.generateStatisticsCommand = GenerateStatisticsWorkflowCommand(self.workflowDirectory)
        self.jobStatistics = None
        self.invocationDataProvider = InvocationDataProvider()
        self.dataTransfer = None
        self.awsContainer = aws_container

    def generate(self):
        return self.generateCommand.execute()

    def plan(self):
        result = self.planCommand.execute()
        self.workflowDirectory = result.split(" ")[2]
        self.dataTransfer = DataTranserService(self.workflowDirectory, self.awsContainer)
        self.generateStatisticsCommand = GenerateStatisticsWorkflowCommand(self.workflowDirectory)
        self.runCommand = RunWorkflowCommand(result)

    def run(self):
        if self.runCommand is not None:
            commands = self.runCommand.execute()
            self.statusCommand = StatusWorkflowCommand(commands['status'])
            self.removeCommand = BaseShellCommand(commands['remove'])

    def status_continuum(self):
        if self.statusCommand is not None:
            statusResult = self.statusCommand.execute()
            while (not statusResult or statusResult['%DONE'] != '100.0'):
                statusResult = self.statusCommand.execute()
                print(statusResult)
                time.sleep(5)

    def remove(self):
        if self.removeCommand is not None:
            self.removeCommand.execute()

    def generate_statistics(self):
        self.jobStatistics = self.generateStatisticsCommand.execute()
        print(self.jobStatistics)
        self.invocationDataProvider.update_transformations(self.workflowDirectory + "/statistics/breakdown.txt")

    def transfer_file(self):
        self.dataTransfer.transfer_directory()
