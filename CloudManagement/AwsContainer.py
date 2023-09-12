class AwsContainer:
    def __init__(self, pem_file, user):
        self.pemFile = pem_file
        self.user = user

    def get_user(self):
        return self.user.split("@")[0]

    def get_ip(self):
        return self.user.split("@")[1]


