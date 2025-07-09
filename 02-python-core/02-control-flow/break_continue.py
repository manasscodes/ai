# Demonstrate break and continue
for i in range(1, 11):
    if i == 5:
        continue  # skip 5
    if i == 8:
        break     # stop at 8
    print(i)