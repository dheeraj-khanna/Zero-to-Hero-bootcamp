import math
import collections


def vol(rad):
    """
    Write a function that computes the volume of a sphere given its radius.
    The volume of a sphere is given as 4/3 π 𝑟 3
    :param rad:
    :return:
    """
    return (4 / 3) * math.pi * (rad ** 3)


# print(vol(2))


def ran_check(num, low, high):
    """
    Write a function that checks whether a number is in a given range (inclusive of high and low)

    :param num:
    :param low:
    :param high:

    :return:

    ran_check(5,2,7) should return "5 is in the range between 2 and 7"

    """

    if low < num < high:
        return f" {num} is in the range between {low} and {high}"
    else:
        return f" {num} is not in the range between {low} and {high}"


# print(ran_check(5, 2, 17))

def up_low(s):
    """
    Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

    HINT: Two string methods that might prove useful: .isupper() and .islower()
    If you feel ambitious, explore the Collections module to solve this problem!
    :param s:

    :return:

    """
    count_upper = 0
    count_lower = 0

    for item in s:
        if item.isupper():
            count_upper += 1
        elif item.islower():
            count_lower += 1

    print(f"No. of Upper case characters : {count_upper}")
    print(f"No. of Lower case Characters : {count_lower}")


# inputStr = "Hello Mr. Rogers, how are you this fine Tuesday?"
# up_low(inputStr)


def unique_list(lst):\

    """
    Write a Python function that takes a list and returns a new list with unique elements of the first list.

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]

    :param lst:

    :return: list

    """

    return list(set(lst))


# sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
# print(unique_list(sample_list))


def multiply(numbers):
    """
    Write a Python function to multiply all the numbers in a list.

    Sample List : [1, 2, 3, -4]
    Expected Output : -24

    :param numbers:

    :return: integer

    """

    multiplied = 1
    for item in numbers:
        multiplied = item * multiplied

    return multiplied


# sample_list = [1, 2, 3, -4]
# print(multiply(sample_list))


def palindrome(s):
    """
    Write a Python function that checks whether a word or phrase is palindrome or not.

    Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g.,
    madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace()
    method in a string to help out with dealing with spaces. Also google search how to reverse a
    string in Python, there are some clever ways to do it with slicing notation.

    :return: boolean

    """

    reverseStr = s[::-1]
    if s == reverseStr:
        return True
    else:
        return False

# print(palindrome('helleh'))
# print(palindrome('racecar'))

import string


def ispangram(strtoCheck, alphabet= string.ascii_lowercase):
    """
    Write a Python function to check whether a string is pangram or not.
    (Assume the string passed in does not have any punctuation)

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

    For example : "The quick brown fox jumps over the lazy dog"

    Hint: You may want to use .replace() method to get rid of spaces.

    :param strtoCheck:

    :param alphabet:

    :return:

    """

    finalStr = ""
    set_finalStr = set()
    lst_lower_str2Check = strtoCheck.lower().split()
    lst_lower_str2Check.sort()
    for item in lst_lower_str2Check:
        finalStr = finalStr + item

    set_finalStr = set(finalStr)
    set_alphabet = set(alphabet)

    if set_finalStr == set_alphabet:
        return True
    else:
        return False


print(ispangram("The quick brown fox jumps over the lazy dog"))
