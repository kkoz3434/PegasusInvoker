from Commands.BaseShellCommand import BaseShellCommand


class GenerateStatisticsWorkflowCommand(BaseShellCommand):
    def __init__(self, workflow_directory):
        BaseShellCommand.__init__(self, "pegasus-statistics -s all " + workflow_directory)
        self.statisticsFiles = {}

    def execute(self):
        result = BaseShellCommand.execute(self)
        self.fill_statistics_dict(result)
        return self.statisticsFiles

    def fill_statistics_dict(self, result):
        lines_iterator = iter(result.split('\n'))
        for line in lines_iterator:
            line = line.strip()
            if line.startswith('Summary'):
                break;
        for line in lines_iterator:
            if(line != ''):
                words = line.split(':')
                self.statisticsFiles[words[0].strip()] = words[1].strip()

