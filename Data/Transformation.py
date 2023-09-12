class Transformation:
    def __init__(self, columns, line):
        self.name = ""
        self.stats = self.fill_stats(columns, line)

    def fill_stats(self, columns, data):
        stats = {}
        self.name = data[0]
        for column, data in zip(columns[1:], data[1:]):
            stats[column] = data
        return stats

    def __str__(self):
        return (self.name + " # " + str(self.stats))
