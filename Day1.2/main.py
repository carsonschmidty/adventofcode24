from Reader import *
from Similarity import *

reader = Reader("input.txt")
data = reader.parse()

sim = Similarity(data[0], data[1])