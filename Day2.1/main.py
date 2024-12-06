from Reader import *
from Counter import *
from p2 import part2

reader = Reader("test.txt")
data = reader.parse()

counter = Counter(data)

print(counter.safe())

with open("input.txt", "r") as file:
    text = file.read()


print(part2(text))