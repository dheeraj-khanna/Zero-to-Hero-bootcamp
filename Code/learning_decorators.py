def func():
    return 1


print(func())


def hello():
    print("Hello")


greet = hello

greet()

del hello

# it will give an error because hello() function is deleted from previous statement.
# hello()

# Notice it will still print the "Hello" string since the name greet is still ponting to
# same object hello().
greet()
