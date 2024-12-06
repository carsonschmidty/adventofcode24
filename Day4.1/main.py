origin = ['X']

path = "input.txt"
data = []
with open(path, "r") as File:
    for line in File:
        fields = line.strip("\n")
        data.append(list(fields))


width = len(data[0])
height = len(data)

def valid(x, y):
    right = [(x+1,y),(x+2,y),(x+3,y)]
    left = [(x-1,y),(x-2,y),(x-3,y)]
    lright = [(x+1,y+1),(x+2,y+2),(x+3,y+3)]
    lleft = [(x-1,y+1),(x-2,y+2),(x-3,y+3)]
    uright = [(x+1,y-1),(x+2,y-2),(x+3,y-3)]
    uleft = [(x-1,y-1),(x-2,y-2),(x-3,y-3)]
    down = [(x,y+1),(x,y+2),(x,y+3)]
    up = [(x,y-1),(x,y-2),(x,y-3)]

    valid = []
    if x > 2:
        valid.append(left)
        if y < height - 3:
            valid.append(lleft)
        if y > 2:
            valid.append(uleft)
    if x < width - 3:
        valid.append(right)
        if y < height - 3:
            valid.append(lright)
        if y > 2:
            valid.append(uright)
    if y > 2:
        valid.append(up)
    if y < height - 3:
        valid.append(down)

    return valid

xmas = ['M','A','S']
frequency = {}
amount = []

def XMAS(x, y, valid, data):
    total = []
    print(valid)
    print(x)
    print(y)
    for v in valid:
        lst = []
        lst.append(data[v[0][1]][v[0][0]])
        lst.append(data[v[1][1]][v[1][0]])
        lst.append(data[v[2][1]][v[2][0]])

        if lst == xmas:
            total.append(lst)
            amount.append(lst)

    key = str(x) + " " + str(y)
    frequency[key] = total

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'X':
            v = valid(x,y)
            print(len(v))
            XMAS(x,y,v,data)
            
print(frequency)
print(len(amount))