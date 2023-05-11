#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    total = 0
    if n == 1:
        print("0")
    else:
        for i in range(1, n):
            arg = int(argv[i])
            total += arg
        print("{}".format(total))
