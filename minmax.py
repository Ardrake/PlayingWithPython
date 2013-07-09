# execfile("./Study/minmax.py")

import time
import random

myList = [ 12, 11, 10, 9, 4, 3, 2, -1, 1000000 ]
testList = []

def findMinMax1(list, min, max):
    i = 0 
    j = len(list) - 1
    while i < j:
        if(list[i] < min):
            min = list[i]
        if(list[j] < min):
            min = list[j]

        if(list[i] > max):
            max = list[i]
        if(list[j] > max):
            max = list[j]

        i += 1
        j -= 1

    print "Min: " + str(min) + " | Max: " + str(max)

def findMinMax2(list):
    print "Min: " + str(min(list)) + " | Max: " + str(max(list))

def findMinMax3(list, minMax):
    if not list:
        return minMax
    elif len(list) == 1:
        if list[0] < minMax[0]:
            minMax[0] = list[0]
        if list[0] > minMax[1]:
            minMax[1] = list[0]
        return minMax
    else:
        if list[0] < minMax[0]:
            minMax[0] = list[0]
        if list[-1] < minMax[0]:
            minMax[0] = list[-1]
        if list[0] > minMax[1]:
            minMax[1] = list[0]
        if list[-1] > minMax[1]:
            minMax[1] = list[-1]
        return findMinMax3(list[1:-1], minMax)

def createList(max=1000):
    for x in range(0,max):
        testList.append(random.randint(-1000000,1000000))

def testMinMax(testLen=1000):
    if not testList or len(testList) != testLen:
        createList(testLen)

    before=time.time();
    findMinMax1(testList, 1000001, -1000001)
    end=time.time()
    print "---- Iterative: " + str(end-before) + " ----"

    before=time.time();
    res = findMinMax3(testList, [1000001, -1000001])
    end=time.time()
    print "Min: " + str(res[0]) + " | Max: " + str(res[1])
    print "---- Recursive: " + str(end-before) + " ----"

    before=time.time();
    findMinMax2(testList)
    end=time.time()
    print "---- System: " + str(end-before) + " ----"
    
# before=time.time(); findMinMax3(myList, [10000000, -10000000]); end=time.time(); end-before
