data = {}
keys = list(data.keys())
values = list(data.values())
empty_dict = {}
for i in range(300):
    empty_dict[values[i]] = keys[i]

print(empty_dict)
