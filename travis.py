knownUsers = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]
print(len(knownUsers))

while True:
    print("Hi! My name is Travis!")
    name = input("What is your name?: ").strip().capitalize()

    if name in knownUsers:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n)").lower()

        if remove == "y":
            knownUsers.remove(name)
        elif remove == "n":
            print("No problem! I didn't want you to leave anyway!")
            
    else:
        print("I don't think I've met you yet!")
        addMe = input("Woud you like to be added to the system (y/n): ").strip().lower()

        if addMe == "y":
            knownUsers.append(name)
        elif addMe == "n":
            print("No problem! You own't be added!")
