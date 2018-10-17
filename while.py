L = []

while len(L) < 3:
    newName = input("Please add a new name: ").strip().capitalize()
    L.append(newName)

print("Sorry list is full")
print(L)
