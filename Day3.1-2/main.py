import re

pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
sum = 0
path = "input.txt"

results = []

with open(path,'r') as File:
    for line in File:
        matches = re.findall(pattern, line)
        for match in matches:
            results.append(match[0])

print(results)

sum = 0 

pattern = r"mul\((\d+),(\d+)\)"

flag = True

for r in results:
    if r.startswith("do()"):
        flag = True
    elif r.startswith("don't"):
        flag = False
    if flag:
        if r.startswith("mul"):
            nums = re.findall(r'\d+', r)
            x,y = map(int, nums)
            sum += x * y


print(sum)