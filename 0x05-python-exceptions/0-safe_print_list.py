#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nums = 0
    try:
        for i in range(x):
            print(my_list[i], sep="", end="")
            nums += 1
    except IndexError:
        pass
    print()
    return nums
