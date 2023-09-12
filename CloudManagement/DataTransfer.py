import subprocess


class DataTranserService:
    def __init__(self, workdir, aws_container):
        self.baseCommand = 'scp -r -i'
        self.pemFilePath = aws_container.pemFile
        self.workdir = workdir
        self.awsUser = aws_container.user
        self.remoteDir = "/home/ubuntu/copied_from_local"
    def transfer_directory(self):
        try:
            command = (self.baseCommand + " " + self.pemFilePath + " " + self.workdir + " " + self.awsUser + ":"
                       + self.remoteDir)
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT,
                                             universal_newlines=True)
            print(result)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Command Failed with Error Code {e.returncode}:")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
