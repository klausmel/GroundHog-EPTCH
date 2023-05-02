#!/usr/bin/python3

def calcul_g(Dict):
    len_g = len(Dict['list'])
    x = len_g - int(Dict['p'])
    result = 0
    tmp = 0

    if int(Dict['p']) < int(Dict['i'] + 1):
        while x != len_g:
            tmp = float(Dict['list'][x]) - float(Dict['list'][x - 1])
            if tmp > 0:
                result = result + tmp
            x = x + 1
    result = result / int(Dict['p'])
    print ("g=", end='')
    if int(Dict['p']) < int(Dict['i'] + 1):
        print ("%.2f" % result, end='    ')
    else:
        print ("nan", end='    ')