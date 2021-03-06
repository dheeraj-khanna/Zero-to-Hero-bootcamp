def lesser_of_two_evens(num1, num2):
    """
    Write a function that returns the lesser of two given numbers if both numbers are even,
    but returns the greater if one or both numbers are odd
    Example :
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5

    :param num1:

    :param num2:

    :return: integer
    """
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        lowest = min(num1, num2)
        return lowest
    else:
        larger = max(num1, num2)
        return larger


# Test the function
# retVal = lesser_of_two_evens(2, 2)
# print(retVal)
# retVal = lesser_of_two_evens(2, 4)
# print(retVal)
# retVal = lesser_of_two_evens(2, 3)
# print(retVal)
# retVal = lesser_of_two_evens(3, 5)
# print(retVal)

def animal_crackers(text):
    """
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    :param text:
    :return: boolean
    
    """
    worldList = text.split()
    if worldList[0][0] == worldList[1][0]:
        return True
    else:
        return False


# retVal = animal_crackers('Levelheaded Llama')
# print(retVal)
# retVal = animal_crackers('Crazy Kangaroo')
# print(retVal)


def makes_twenty(num1, num2):
    """
    MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
    If not, return False

    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False

    :param num1:
    :param num2:

    :return:

    """
    num1 = int(num1)
    num2 = int(num2)
    num3 = num1 + num2

    if num1 == 20 or num2 == 20 or num3 == 20:
        return True
    else:
        return False


# Should return True
# print(makes_twenty(20, 10))
#
# # Should return True
# print(makes_twenty(12, 8))
#
# # Should return False
# print(makes_twenty(2, 3))

def old_macdonald(inputString):
    """
    OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    old_macdonald('macdonald') --> MacDonald
    Note: 'macdonald'.capitalize() returns 'Macdonald'
    :param inputString:
    :return:
    """
    capitalizeStr = ""
    for index in range(0, len(inputString), 1):
        if index == 0 or index == 3:
            capitalizeStr = capitalizeStr + inputString[index].upper()
        else:
            capitalizeStr = capitalizeStr + inputString[index]

    return capitalizeStr


# It should return --> MacDonald
# print(old_macdonald('macdonald'))

def master_yoda(inputStr):
    """
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'

    :param inputStr:

    :return:
    """
    reverseString = ""
    # splitString = inputStr.split()
    # for index in range(len(splitString)-1, -1, -1):
    #     reverseString = reverseString + splitString[index] + " "

    reverseString.join(inputStr.split())

    return reverseString


# print(master_yoda('I am home'))

def almost_there(number):
    """
    ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    :param number:
    :return: boolean

    """
    if (90 <= number <= 110) or (200 <= number <= 210):
        return True
    else:
        return False


# print(almost_there(90))
# print("===============")
# print(almost_there(104))
# print("===============")
# print(almost_there(150))
# print("===============")
# print(almost_there(209))
# print("===============")

def has_33(num):
    """
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) ??? True
    has_33([1, 3, 1, 3]) ??? False
    has_33([3, 1, 3]) ??? False

    :param num:
    :return: boolean

    """

    numList = []
    position_of_3 = []
    numList = num
    count3 = numList.count(3)
    counter = 0

    for counter in range(len(numList)):
        if count3 > 1:
            if numList[counter] == 3:
                if numList[counter] == numList[counter + 1]:
                    return True
                else:
                    numList.pop(numList.index(3))
                    count3 = numList.count(3)
                    counter += 1
            else:
                continue
        else:
            return False


# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

def paper_doll(inputStr):
    """
    PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

    :param inputStr:

    :return:

    """
    finalStr = ""

    for item in inputStr:
        finalStr = finalStr + 3 * item

    return finalStr


# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))


def blackjack(num1, num2, num3):
    """

    BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum is less than 31 and there's an eleven, reduce the total sum by 10. Finally, if the sum
    (even after adjustment) exceeds 21, return 'BUST'

    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19

    :param num1:

    :param num2:

    :param num3:

    :return: integer / BUST

    """

    # total = num1 + num2 + num3
    # if total <= 21:
    #     return total
    # else:
    #     if (total <= 31) and (num1 == 11 or num2 == 11 or num3 == 11):
    #         total = total - 10
    #         return total
    #     else:
    #         return "BUST"
    # Nice way of it

    if sum((num1, num2, num3)) <= 21:
        return sum((num1, num2, num3))
    else:
        if sum((num1, num2, num3)) <= 31 and 11 in (num1, num2, num3):
            return sum((num1, num2, num3)) - 10
        else:
            return "BUST"


# print(blackjack(5,6,7))     #--> 18
# print(blackjack(9,9,9))     #--> 'BUST'
# print(blackjack(9,9,11))    #--> 19

def summer_69(arr):
    """
    SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting
    with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
    Return 0 for no numbers.

    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14

    :param arr:

    :return: 0 or no number

    """
    total = 0
    skip = False
    for num in arr:
        if num != 6 and skip is False:
            total = total + num
        elif num == 6:
            skip = True
            continue
        elif num == 9:
            skip = False
            continue

    return total


# # --> 9
# print(summer_69([1, 3, 5]))
#
# # --> 9
#
# print(summer_69([4, 5, 6, 7, 8, 9]))
#
# # #--> 14
#
# print(summer_69([2, 1, 6, 9, 11]))

def spy_game(nums):
    """
    SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

    spy_game([1,2,4,0,0,7,5]) --> True

    spy_game([1,0,2,4,0,5,7]) --> True

    spy_game([1,7,2,0,4,5,0]) --> False

    :param nums:

    :return:

    """
    # found_0 = False
    # found_0_0 = False
    # found_0_0_7 = False
    #
    # for index in range(0, len(nums), 1):
    #     if (nums[index] == 0) and (found_0 is False):
    #         found_0 = True
    #     elif (nums[index] == 0) and (found_0 is True) and (found_0_0 is False):
    #         found_0_0 = True
    #     elif (nums[index] == 7) and (found_0 is True) and (found_0_0 is True):
    #         found_0_0_7 = True
    #         return found_0_0_7
    #
    # return False

# better and simplified version
#     to_be_found = [0, 0, 7, 'x']
#     for item in nums:
#         if item == to_be_found[0]:
#             to_be_found.pop(0)
#
#     return len(to_be_found) == 1
#
#
# # --> True
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
#
# # --> True
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
#
# # --> False
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))


def count_primes(num):

    """
    COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and
    including a given number

    count_primes(100) --> 25
    By convention, 0 and 1 are not prime.

    :param num:
    :return: integer
    """
    # write a small function to check if the number is prime or not

    def is_prime(number):
        index = 2
        for index in range(index, number, 1):
            if number % index == 0:
                return False
            else:
                continue

        return True

    count_of_prime = set()

    for prime in range(2, num, 1):
        if is_prime(prime):
            count_of_prime.add(prime)

    return len(count_of_prime)

# print(count_primes(1000))


def print_BIG(letter):

    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


# print_BIG('a')
# print_BIG('b')
# print_BIG('c')
# print_BIG('d')
# print_BIG('e')