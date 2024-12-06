class Reader:
    def __init__(self, path, delimiter=" "):
        self.path = path
        self.delimiter = delimiter

    def parse(self):
        data = []

        with open(self.path, 'r') as file:
            for line in file:
                fields = line.strip().split(self.delimiter)
                for i in range(len(fields)):
                    fields[i] = int(fields[i])
                data.append(fields)

        return data

