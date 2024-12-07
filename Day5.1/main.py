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

print (rules)
print (updates)

