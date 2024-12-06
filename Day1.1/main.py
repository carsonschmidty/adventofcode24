from Sort import *
from Reader import *

reader = Reader("input.txt")
data = reader.parse()

sorter = Bubble(data[0], data[1])
sorter.compare()
sorter.print_sorted()
sorter.distance()
