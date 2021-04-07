from random import randint

wordList = ["Apple", "Cherry", "Pear", "Strawberry"]

def askGuess(theWord):
    userInput = input("Guess a letter\n").lower()
    gameBoard = list(len(theWord)*("-"))
    
    count = 0
    match = False
    amount = 0

    for i in theWord:
        if i == userInput:
            gameBoard[count] = i
            match = True
            amount += 1
            count += 1
        else:
            count += 1
    
    if match == True:
        print("There are " + str(amount) + " " + userInput + "(s)")
        print("".join(gameBoard))
    else:
        print("No matches. Try again.")


word = wordList[randint(0, len(wordList) - 1)]

