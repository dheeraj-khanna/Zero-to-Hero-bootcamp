def printWordStartWithLetter(word, letter):
    """
    # Use for, .split(), and if to create a Statement that will print out words that start with 's':
    :return:

    """
    my_list = []
    retStr = word.split()
    print(retStr)
    # =============
    # Basic version
    # ==============
    # for index in range(0, len(retStr)):
    #     value = retStr[index]
    #     if value.startswith('s'):
    #         my_list.append(retStr[index])
    # ===============
    # Simplified version
    # ==============
    # for value in retStr:
    #     if value.startswith('s'):
    #         my_list.append(value)
    # ================
    # using list comprehensions
    # read this like element for element in list if element.startswith('s') than add that to my_list list
    # ================
    my_list = [value for value in retStr if value.startswith('s')]

    print(my_list)

# inputStr = 'Print only the words that start with s in this sentence'
# inputLetter = 's'
# printWordStartWithLetter(inputStr, inputLetter)



def printAllEvenNumbersinRange():

    evenNumList = []
    evenNumList = [evenNumber for evenNumber in range(0, 11, 1) if evenNumber % 2 == 0]
    print(evenNumList)


# printAllEvenNumbersinRange()


def printAllNumbersDivByThree():

    evenNumList = []
    evenNumList = [evenNumber for evenNumber in range(1, 50, 1) if evenNumber % 3 == 0]
    print(evenNumList)


# printAllNumbersDivByThree()


def printEvenLengthWord():
    """
    Go through the string below and if the length of a word is even print "even!"
    st = 'Print every word in this sentence that has an even number of letters'
    :return:
    """

    sentence = 'Print every word in this sentence that has an even number of letters'
    wordList = sentence.split()
    evenLenWordList = [word for word in wordList if len(word) % 2 == 0]
    print(evenLenWordList)


# printEvenLengthWord()

def printFizzBuzz():
    """
    Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
    instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples
    of both three and five print "FizzBuzz".

    :return: None
    """
    my_list = [index for index in range(1, 101, 1)]
    for listIndex in range(1, len(my_list), 1):
        if (my_list[listIndex] % 3 == 0) and (my_list[listIndex] % 5 == 0):
            my_list[listIndex] = "FizzBuzz"
            continue
        elif my_list[listIndex] % 3 == 0:
            my_list[listIndex] = "Fizz"
        elif my_list[listIndex] % 5 == 0:
            my_list[listIndex] = "Buzz"

    print(my_list)


# printFizzBuzz()

def createListFirstLetter():

    """
    Use List Comprehension to create a list of the first letters of every word in the string below:
    st = 'Create a list of the first letters of every word in this string'

    :return: None

    """
    letterList = []
    sentence = 'Create a list of the first letters of every word in this string'
    print(sentence)
    wordList = sentence.split()
    for index in range(0,len(wordList)):
        letterList.append(wordList[index][0])
    print(letterList)

# createListFirstLetter()