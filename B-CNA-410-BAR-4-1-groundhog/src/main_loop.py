#!/usr/bin/python3

from src.calcul_g import calcul_g
from src.calcul_r import calcul_r
from src.calcul_s import calcul_s

# syntax: identical values
# correct number of switches

def print_switch(Dict):
    if Dict['before_r'] < 0 and Dict['actual_r'] > 0:
        print("     a switch occurs")
        Dict['switch'] = Dict['switch'] + 1
    elif Dict['before_r'] > 0 and Dict['actual_r'] < 0:
        print("     a switch occurs")
        Dict['switch'] = Dict['switch'] + 1
    else:
        print("")

def try_float(nb):
    try:
        float(nb)
    except ValueError:
        return False
    else:
        return True

def weird_values(Dict):
    i = 1
    x = 0
    len_list = len(Dict['list'])
    result_list = [0, 0, 0, 0, 0]

    Dict['list'] = sorted(Dict['list'])
    while x < len_list and x != 5:
        result_list[x] = Dict['list'][x]
        x = x + 1

    print("5 weirdest values are [", end='')
    while i != 6:
        if i + 1 != 6:
            print("%.2f" % result_list[i - 1],  end=', ')
        else:
            print("%.2f" % result_list[i - 1], end='')
        i = i + 1
    print("]")


def main_loop(argv):
    Dict = {'input': 0, 'p': argv[1] ,'i': 0, 'list': [], 'before_r': 0, 'actual_r': 0, 'switch': 0}
    while Dict['input'] != "STOP":
        Dict['input'] = input()
        if not try_float(Dict['input']) and Dict['input'] != "STOP" and Dict['input'] != "":
            return 84
        if (Dict['input'] != "STOP" and Dict['input'] != ""):
            Dict['list'].append(float(Dict['input']))
            calcul_g(Dict)
            calcul_r(Dict)
            calcul_s(Dict)
            print_switch(Dict)
            Dict['i'] = Dict['i'] + 1
    print("Global tendency switched %d times" % Dict['switch'])
    weird_values(Dict)
    if Dict['input'] == "STOP" and Dict['i'] < int(argv[1]):
        return 84