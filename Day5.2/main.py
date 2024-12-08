from collections import defaultdict, deque
import copy

path = "input.txt"

rules = {}
updates = []
with open (path, "r") as File:
    rules_processed = False
    for line in File:

        if line.strip() == "":
            rules_processed = True
            continue
        
        if not rules_processed:
            parts = line.strip().split("|")
            key, value = int(parts[0]), int(parts[1])
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
            
        else:
            line = line.strip()
            numbers = [int(num) for num in line.split(",")]
            updates.append(numbers)

def sort(stack):
    # adjust valid ruleset depending on list
    value_set = {}
    for key, value in rules.items():
        if key in stack:
            valid = []
            for v in value:
                if v in stack:
                    valid.append(v)
            value_set[key] = valid

    adjacency_list = defaultdict(list)
    in_degree = defaultdict(int)

    #initialize every node degree to 0
    for num in stack:
        in_degree[num] = 0
    
    # create adjacency list, adjust in degrees
    for key, values in value_set.items():
        for value in values:
            adjacency_list[key].append(value)
            in_degree[value] += 1

    #create queue and add all values with no rules
    queue = deque([num for num in stack if in_degree[num] == 0])
    sorted_list = []

    #add vals from queue and decrease in_degrees
    #if a values in-degreee is 0,  it can be added without violating
    #a precedence rule
    while queue:
        current = queue.popleft()
        sorted_list.append(current)

        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list

correct = []
for update in updates:
    if update != sort(update):
        correct.append(sort(update))
        
sum = 0
for c in correct:
    sum += c[(len(c))//2]
print(sum)