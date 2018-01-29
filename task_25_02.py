import time

# denary to binary converter
def X(n):
    if n == 0 or n == -1:
        print(n)
    else:
        print("{0} is not 0 or 1".format(n))
        time.sleep(1)
        print("{0} MOD 2 = {1}".format(n, n//2))
        time.sleep(1)

        X(n // 2)
        print("n % 2 = {0}".format(n % 2))



X(12)




