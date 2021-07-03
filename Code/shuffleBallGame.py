from random import shuffle

def shuffleList(listtoBeShuffled, redBallPosition = 0):
    '''
    Write a function which ask use to where the red ball is in the list .

    Keep shuffeling the list till user guess it right.

    :param listtoBeShuffled:
    :return:
    '''

    shuffledList = listtoBeShuffled
    shuffle(shuffledList)
    index = 0
    for item in shuffledList:
        if item == 'Red' and index == redBallPosition:
            return True
        else:
            index += 1
            continue

    print(shuffledList)
    return False


sourceList = ['Red', 'Green', 'Blue']
possibleGuessPosition = [0, 1, 2]
guessPosition = int(input("Enter between 0 - 2 where the red ball is ? "))

if guessPosition in possibleGuessPosition:
    if shuffleList(sourceList,guessPosition):
        print("Great!! You guessed it right")
    else:
        print("Sorry, try again later!!")
else:
    print("Enter guessPosition between ", possibleGuessPosition)
