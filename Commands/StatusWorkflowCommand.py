from Commands.BaseShellCommand import BaseShellCommand


class StatusWorkflowCommand(BaseShellCommand):
    def __init__(self, command):
        BaseShellCommand.__init__(self,command)
        # dictionary with status information with keys:
        # UNRDY READY   PRE  IN_Q  POST  DONE  FAIL %DONE STATE DAGNAME
        self.results = {}

    def execute(self):
        result = BaseShellCommand.execute(self)
        self.parse_result_to_dictionary(result)
        return self.results

    def parse_result_to_dictionary(self, result):
        lines_iterator = iter(result.split('\n'))
        for line in lines_iterator:
            line = line.strip()
            if line.startswith('UNRDY'):
                keys = line.split()
                values = str(next(lines_iterator)).split()
                self.results = dict(zip(keys, values))
                return




