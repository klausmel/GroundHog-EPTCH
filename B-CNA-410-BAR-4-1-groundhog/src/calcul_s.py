#!/usr/bin/python3

from math import sqrt

def calcul_s(Dict):
    result = 0

    if int(Dict['p']) <= int(Dict['i'] + 1):
        result = sum(Dict['list'][- int(Dict['p']):]) 
        result = result / int(Dict['p'])
        result = sum(map(lambda x:(x - result)**2, Dict['list'][- int(Dict['p']):])) / int(Dict['p'])
        result = sqrt(result)
    print ("s=", end='')
    if int(Dict['p']) <= int(Dict['i'] + 1):
        print ("%.2f" % result, end='')
    else:
        print ("nan", end='')