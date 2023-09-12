import paramiko

class BaseCloudShellCommand:
    def __init__(self, aws_container,  command=""):
        self.command = command
        self.awsContainer = aws_container

    def execute(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            private_key = paramiko.RSAKey.from_private_key_file(self.awsContainer.pemFile)
            username = self.awsContainer.get_user()
            ssh.connect(self.awsContainer.get_ip(), username=username, pkey=private_key)
            stdin, stdout, stderr = ssh.exec_command(self.command)
            print("SSH Output:")
            print(stdout.read().decode("utf-8"))
        except paramiko.SSHException as e:
            print(f"SSH connection error: {str(e)}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            ssh.close()
