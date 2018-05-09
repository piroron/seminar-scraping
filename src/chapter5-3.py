values = {}

values["apple"] = 120
values["orange"] = 100
values["banana"] = 80

total = 0

for key, value in values.items():
    print(key + ":" + str(value))
    total += value
print("total:" + str(total))