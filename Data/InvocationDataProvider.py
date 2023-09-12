from Data.Transformation import Transformation


class InvocationDataProvider:
    def __init__(self):
        self.transformations = {}

    def update_transformations(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        columns = ''
        lines_iterator = iter(lines)
        for line in lines_iterator:
            if not line.startswith("#") and line != "\n":
                columns = line.split()
                break

        for line in lines_iterator:
            if line == '\n':
                break
            splitted = line.split()
            self.transformations[splitted[0]] = Transformation(columns, splitted)

        for value in self.transformations.values():
            print(str(value))




