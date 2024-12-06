class Sort:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

        self.sortedarr1 = []
        self.sortedarr2 = []

    def distance(self):
        distance_sum = 0
        for x in range(len(self.array1)):
            distance_sum += abs(self.array1[x] - self.array2[x])
        print(distance_sum)
        return distance_sum
    def print_sorted(self):
        print(self.sortedarr1)
        print(self.sortedarr2)

class Bubble(Sort):
    def compare(self):
        self.sortedarr1 = self.sort(self.array1)
        self.sortedarr2 = self.sort(self.array2)

    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
