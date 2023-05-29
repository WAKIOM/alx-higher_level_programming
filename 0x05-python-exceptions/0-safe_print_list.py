#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nums = 0
    for item in my_list:
        try:
            print(f"{item}", end="")
            nums += 1
        except IndexError:
            break
    print()
    return nums
