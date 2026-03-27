import random

accepted_values = set()

while len(accepted_values) < 10:
    i = random.randint(0, 9)        # integer 0–9
    x = i + random.random()         # add random float (0 to 1)

    # round to avoid floating precision duplicates being weird
    x = round(x, 5)

    if x not in accepted_values:
        accepted_values.add(x)

# convert to list if you want
result = list(accepted_values)

print(result)
