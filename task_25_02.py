import time

# denary to binary converter
def X(n):
    if n == 0 or n == 1:
        print("it equals 0 or one")
        time.sleep(1)
        print("        {0}".format(n))
    else:
        print("{0} was not 0 or 1".format(n))
        time.sleep(1)

        print("{0} // 2 = {1}".format(n, n // 2))
        time.sleep(1)
        print("{0} is sent to X".format(n // 2))
        time.sleep(1)
        X(n // 2)
        print("{1} % 2 = {0}".format(n % 2, n))



X(12)




