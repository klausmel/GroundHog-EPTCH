#!/usr/bin/python3

from sys import argv, exit

from src.error_handling import error_handling
from src.main_loop import main_loop

def main():
    if error_handling(argv) == 84:
        return 84
    return (main_loop(argv))

if __name__ == '__main__':
    exit(main())