"""

Overview of Regular Expressions

Regular Expressions (sometimes called regex for short) allows a user to search for strings using almost any sort of
rule they can come up. For example, finding all capital letters in a string, or finding a phone number in a document.

Regular expressions are notorious for their seemingly strange syntax. This strange syntax is a byproduct of their
flexibility. Regular expressions have to be able to filter out any string pattern you can imagine, which is why they
have a complex string pattern format.

Let's begin by explaining how to search for basic patterns in a string!

Character	Description	                ExamplePattern      Code
\d	        A digit	                    file_\d\d	        file_25
\w	        Alphanumeric	            \w-\w\w\w	        A-b_1
\s	        White space	                a\sb\sc	            a b c
\D	        A non digit	                \D\D\D	            ABC
\W	        Non-alphanumeric            \W\W\W\W\W	        *-+=)
\S	        Non-whitespace	            \S\S\S\S	        Yoyo
+	        Occurs one or more times    Version \w-\w+	    Version A-b1_1
{3}	        Occurs exactly 3 times	    \D{3}	            abc
{2,4}	    Occurs 2 to 4 times	        \d{2,4}	            123
{3,}	    Occurs 3 or more	        \w{3,}	            anycharacters
\*	        Occurs zero or more times	A\*B\*C*	        AAACC
?	        Once or none	            plurals?	        plural

"""

import re


def basic_patterns(text=""):
    text = "The agent's phone number is 408-555-1234. Call soon!"

    pattern = "phone"
    match = re.search(pattern, text)
    print(match)
    text = "The agent's phone number is 408-522-1111. Call soon!"
    ###
    # NOTES : \d means that it is an integer. Repeated expression of \d denotes the number of times.
    ###
    match = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
    print(match)
    print(match.group())


# basic_patterns()


def basic_patterns_with_quantifier(text=""):
    text = "The agent's phone number is 678-522-1111. Call soon!"
    ###
    # NOTES : \d means that it is an integer , {3} means that number mentioned as \d is three digits
    ###

    match = re.search(r'\d{3}-\d{3}-\d{4}', text)
    print(match)
    print(match.group())

    text = "The agent's phone number is 678-522-1111. Call soon!"
    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    print(phone_pattern)
    results = re.search(phone_pattern, text)

    # print the whole group
    print(results.group())
    # prints 678 as group 1
    print(results.group(1))
    # prints 522 as group 2
    print(results.group(2))
    # prints 1111 as group 3
    print(results.group(3))
    # error since there is no 4th group
    # print(results.group(4))


# basic_patterns_with_quantifier()


def pattern_with_operators(text=""):
    """
    Additional Regex Syntax
    Or operator |
    Use the pipe operator to have an or statement.

    :param text:
    :return:
    """
    # result = re.search(r"man|woman", "This man was here.")
    # print(result)
    #
    # result = re.search(r"man|woman", "This woman was here.")
    # print(result)
    #
    # result = re.findall(r"at", "This woman was is having a hat and sat with a cat.")
    # print(result)
    #
    # result = re.findall(r".at", "This woman was is having a hat and sat with a cat.")
    # print(result)
    #
    # # '^ means starts with and postfix of \d denotes that a number. ' \
    # # 'English translation of ^\d in statement below is find a sentense start with a number' \
    # # 'Thats why you will get only 1 from the example mentined below.'
    # result = re.findall(r"^\d", "1 is a number")
    # print(result)

    # 'in this example we wont find anything since we are using '\
    # 'pattern for starts with and number comes in the end'

    # result = re.findall(r"^\d", "number in this sentence is 1")
    # print(result)

    # 'in this example we will find the desired string since we are using '\
    # 'pattern for ends with and number comes in the end'

    # result = re.findall(r"\d$", "number in this sentence is 1")
    # print(result)

    # How to use [] for Exclusion
    # To exclude characters, we can use the ^ symbol in conjunction with a set of brackets [].
    # Anything inside the brackets is excluded. For example:

    phrase = "there are 3 numbers 34 inside 5 this sentence."
    # [] is used for exclusion the identifier mentioned inside the sqaure bracket
    # result = re.findall(r'[^\d]', phrase)
    # print(result)

    # Observe the output of it and compare it with the previous statement.
    # To get the words back together, use a + sign
    # result = re.findall(r'[^\d]+', phrase)
    # print(result)

    # test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
    # # the below pattern is excluding "!", "." , "?" from the phrase
    # result = re.findall(r'[^!.?]+', test_phrase)
    # print(result)

    # test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
    # # the below pattern is excluding "!", "." , "?" from the phrase and whitespace between words
    # result = re.findall(r'[^!.? ]+', test_phrase)
    # print(result)
    # # join the result back as sentence
    # back_to_sentence = ' '.join(result)
    # print(back_to_sentence)

    # How to use Brackets for grouping and inclusions
    # find the number of letters before and after hyphen (-)
    # text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
    # result = re.findall(r'[\w]+-[\w]+', text)
    # print(result)

    # Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
    text = 'Hello, would you like some catfish?'
    texttwo = "Hello, would you like to take a catnap?"
    textthree = "Hello, have you seen this caterpillar?"

    result = re.search(r'cat(fish|nap|claw)', text)
    print(result)

    result = re.search(r'cat(fish|nap|claw)', texttwo)
    print(result)

    result = re.search(r'cat(fish|nap|claw)', textthree)
    print(result)

    result = re.search(r'cat(fish|nap|erpillar)', textthree)
    print(result)


pattern_with_operators()
