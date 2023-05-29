#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nums = 0
    try:
        for item in my_list:
            if nums < x:
                print(item, end="")
                nums += 1
    except IndexError:
        pass
    print()
    return nums
