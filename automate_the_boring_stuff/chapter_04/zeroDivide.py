def spam_original(divide_by):
    return 42 / divide_by

def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


try:
    print(spam_original(2))
    print(spam_original(12))
    print(spam_original(0))
    print(spam_original(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')