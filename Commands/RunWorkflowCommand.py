from Commands.BaseShellCommand import BaseShellCommand


class RunWorkflowCommand(BaseShellCommand):
    def __init__(self, command):
        BaseShellCommand.__init__(self, command)
        self.resultStatusCommand = ""
        self.resultRemoveCommand = ""

    def execute(self):
        result = BaseShellCommand.execute(self)
        self.extract_status_remove_commands(result)
        return {"status": self.resultStatusCommand, "remove": self.resultRemoveCommand}

    def extract_status_remove_commands(self, result):
        for line in result.split('\n'):
            line = line.strip()
            if line.startswith('pegasus-status'):
                print("STATUS COMMAND: " + line)
                self.resultStatusCommand = line
            if line.startswith('pegasus-remove'):
                print("REMOVE COMMAND: " + line)
                self.resultRemoveCommand = line
