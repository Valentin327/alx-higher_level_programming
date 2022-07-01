#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    num = len(sys.argv)
    if num == 1:
        print("{}".format(num - 1))
    elif num == 2:
        print("{}".format(int(sys.argv[num - 1])))
    else:
        for i in range(1, num):
            result = result + int(sys.argv[i])
        print("{}".format(result))
