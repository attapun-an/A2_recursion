"""
base 0! = 1
n! = n * (n-1)!
"""
# recursion is basically calling one self

# Variables


def num_inp():
    valid = False
    while not valid:
        try:
            x = int(input("Enter number: "))
            valid = True
        except ValueError:
            print("Please enter a number")
    return x

# Logic


def fact(n):
    if n == 0:
        ans = 1
    else:
        ans = n * fact(n-1)
    return ans


print(fact(num_inp()))




