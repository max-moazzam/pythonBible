#Game of tic tac toe

def tictactoe():

    #Creates the board
    board = [" " for i in range(9)]

    #Prints the board
    def printBoard():
        row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
        row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
        row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    #Tells which players move it is and puts an X or O in the correct location
    def playerMove(icon):
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2
            
        print("Your turn player {}!".format(number))

        #Takes a number on the board
        while True:
            #Will keep asking for an input until a valid choice is made
            try:
                choice = int(input("Enter your input (1-9): ").strip())

                #Exits loop if a valid choice is made
                if choice == 1 or choice == 2 or choice == 3 or \
                   choice == 4 or choice == 5 or choice == 6 or \
                   choice == 7 or choice == 8 or choice == 9:
                    break
                print()
                print("Invalid input!")
                print()
            except ValueError:
                print()
                print("Invalid input!")
                print()
                continue
            else:
                continue
            
        #Subtracts 1 from the choice since beginning is 1 not 0
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        #If a spot is already taken, go again
        else:
            print()
            print("That space is already taken, go again!")
            printBoard()
            playerMove(icon)

    #Checks for a victory
    def victory(icon):
            #Row1, Row2, Row3, Col1, Col2, Col3, Diag1, Diag2
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
           (board[3] == icon and board[4] == icon and board[5] == icon) or \
           (board[6] == icon and board[7] == icon and board[8] == icon) or \
           (board[0] == icon and board[3] == icon and board[6] == icon) or \
           (board[1] == icon and board[4] == icon and board[7] == icon) or \
           (board[2] == icon and board[5] == icon and board[8] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon) or \
           (board[2] == icon and board[4] == icon and board[6] == icon):
               return True
        else:
            return False           

    #Will return a false value until there are no blank spaces left
    def reset():
        for i in range(9):
            if board[i] == " ":
                return False
        return True

    #Will print board, then player move, then check the victory, loop continues until victory
    while True:

        printBoard()

        #First player moves
        playerMove("X")
        printBoard()
        if victory("X") == True:
            while True:
                playAgain = input("Congratulations, Player 1 has won! Go again? (y/n): ").strip().upper()
                if playAgain == "Y":
                    tictactoe()
                elif playAgain == "N":
                    print("Game Over!")
                    break
                else:
                    print("Invalid input!")
                    continue
                break
            break

        #Resets the board if all options exhausted
        if reset() == True:
             print()
             print("All moves exhausted, board will reset")
             print()
             tictactoe()

        #Second player moves
        playerMove("O")
        if victory("O"):
            printBoard()
            while True:
                playAgain = input("Congratulations, Player 2 has won! Go again? (y/n): ").strip().upper()
                if playAgain == "Y":
                    tictactoe()
                elif playAgain == "N":
                    print("Game Over!")
                    break
                else:
                    print("Invalid input!")
                    continue
                break
            break
