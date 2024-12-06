origin = ['X']

path = "input.txt"
data = []
with open(path, "r") as File:
    for line in File:
        fields = line.strip("\n")
        data.append(list(fields))


width = len(data[0])
height = len(data)

mas = ['M','A','S']
sam = ['S','A','M']
frequency = {}

def valid(x, y):
    rdiag = [(x-1,y+1),(x+1,y-1)]
    ldiag = [(x-1,y-1),(x+1,y+1)]

    valid = []
    if x > 0 and x < width-1 and y > 0 and y < height-1:
        valid.append(rdiag)
        valid.append(ldiag)
    return valid


def XMAS(x, y, valid, data):
    total = []

    for v in valid:
        lst = []
        lst.append(data[v[0][1]][v[0][0]])
        lst.append(data[y][x])
        lst.append(data[v[1][1]][v[1][0]])

        if lst == mas or lst == sam:
            total.append(lst)

    key = str(x) + " " + str(y)
    frequency[key] = total

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'A':
            v = valid(x,y)
            XMAS(x,y,v,data)

count=0
for key, value in frequency.items():
    if len(value) == 2:
        count+=1

print(count)
