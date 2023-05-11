#!/usr/bin/python3.8
if __name__ == '__main__':
    import hidden_4
    for lst in dir(hidden_4):
        if not lst.startswith("__"):
            print("{}".format(lst))
