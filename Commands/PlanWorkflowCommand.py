import os
import subprocess

from Commands import BaseShellCommand


class PlanWorkflowCommand(BaseShellCommand.BaseShellCommand):
    def __init__(self, yml_file):
        self.baseCommand = "pegasus-plan "
        self.commandOptions = {
            '--conf':'pegasus.properties',
            '--dir': 'submit',
            '--sites': 'condorpool',
            '--output-sites': 'local',
            '--cleanup': 'leaf',
            '--force': ''
        }
        self.resultRunCommand = ""
        self.commandArgs = yml_file

    def options_to_string(self):
        options = ""
        for key, value in zip(self.commandOptions.keys(), self.commandOptions.values()):
            options += key + " " + value + " "
        return options

    def execute(self):
        self.command = self.baseCommand + " " + self.options_to_string() + self.commandArgs
        result = BaseShellCommand.BaseShellCommand.execute(self)
        self.set_next_run_directory(result)
        return self.resultRunCommand

    def set_next_run_directory(self, result):
        for line in result.split('\n'):
            line = line.strip()
            if line.startswith('pegasus-run'):
                print("PLAN COMMAND: " + line)
                self.resultRunCommand = line
                return
