class Reader:
    def __init__(self, path, delimiter="   "):
        self.path = path
        self.delimiter = delimiter

    def parse(self):
        data1 = []
        data2 = []

        with open(self.path, 'r') as file:
            for line in file:
                fields = line.strip().split(self.delimiter)
                data1.append(int(fields[0]))
                data2.append(int(fields[1]))
        print(data1)
        print(data2)
        parsed_data = [data1, data2]
        return parsed_data
