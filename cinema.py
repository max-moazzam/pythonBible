films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12,5]
    }

while True:
    
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #Check user age
        if age >= films[choice][0]:

            #Check enough seats
            numSeats = films[choice][1]
            
            if numSeats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("There are not enough seats!")
        else:
            print("You are too young to see that film!")
            
    else:
        print("We don't have that film")
    

