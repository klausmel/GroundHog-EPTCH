#!/usr/bin/python3

def calcul_r(Dict):
    len_list = len(Dict['list'])
    result = 0.00

    if int(Dict['p']) < int(Dict['i'] + 1):
        result = Dict['list'][len_list - int(Dict['p']) - 1]
        if result * 100 == 0:
            print ("r=", end='')
            print ("nan%", end='    ')
            return (0)
        else:
            result = round((Dict['list'][len_list - 1] - result) / result * 100)
    print ("r=", end='')
    Dict['before_r'] = Dict['actual_r']
    Dict['actual_r'] = result
    if int(Dict['p']) < int(Dict['i'] + 1):
        print ("%d%%" % result, end = '    ')
    else:
        print ("nan%", end='    ')