import os
import subprocess


class BaseShellCommand:
    def __init__(self, command=""):
        self.command = command

    def execute(self):
        try:
            # Run the shell command and capture its output
            result = subprocess.check_output(self.command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            # 'result' now contains the output of the shell command as a string
            # print("Command Output:")
            # print(result)
            return result
        except subprocess.CalledProcessError as e:
            # If the command returns a non-zero exit status, an exception is raised
            print(f"Command Failed with Error Code {e.returncode}:")
            print(e.output)
        except Exception as e:
            print(f"An error occurred: {str(e)}")