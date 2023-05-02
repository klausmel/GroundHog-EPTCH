#!/usr/bin/python3

def usage():
    print("SYNOPSIS")
    print("     ./groundhog period\n")
    print("DESCRIPTION")
    print("     period       the number of days defining a period")

def try_int(nb):
    try:
        int(nb)
    except ValueError:
        return False
    else:
        return True

def error_handling(argv):
    argc = len(argv)

    if argc == 2 and argv[1] == "-h" or argc == 1:
        usage()
        return (84)
    if argc != 2:
        usage()
        return (84)
    if not try_int(argv[1]):
        print("period must be an integer")
        return (84)
    if int(argv[1]) <= 0:
        print("period must be more than 0")
        return (84)
    return (0)