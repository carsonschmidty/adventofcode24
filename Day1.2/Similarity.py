class Similarity:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

        self.findSimilarity()
    def findSimilarity(self):
        frequency_table = dict()
        for x in self.array2:
            if x not in frequency_table:
                frequency_table[x] = 1
            else:
                frequency_table[x] += 1

        print(frequency_table)

        similarity_score = 0

        for x in self.array1:
            if x in frequency_table:
                similarity_score += x * frequency_table[x]

        print(similarity_score)
