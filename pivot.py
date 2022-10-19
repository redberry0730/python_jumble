import random

def quickselect_onepivot(l, k, count):
    length = len(l)

    pivot = l[random.randint(0, length-1)]

    l_small = []
    l_big = []

    for i in l:
        if pivot > i:
            l_small.append(i)
        elif pivot < i:
            l_big.append(i)
    assert(length == len(l_small) + len(l_big) + 1)
    if k <= len(l_big):
        res = quickselect_onepivot(l_big, k, count + 1)
        return res
    elif k > len(l_big) + 1:
        res = quickselect_onepivot(l_small, k - len(l_big) - 1, count + 1)
        return res
    else:
        return pivot, count

def quickselect_twopivot(l, k, count):
    length = len(l)

    if length == 1:
        return l[0], count

    pivot_1 = l[random.randint(0, length-1)]
    pivot_2 = l[random.randint(0, length-1)]

    while pivot_2 == pivot_1:
        pivot_2 = l[random.randint(0, length-1)]

    l_small = []
    l_between = []
    l_big = []

    if pivot_1 > pivot_2:
        upper_bound = pivot_1
        lower_bound = pivot_2
    else:
        upper_bound = pivot_2
        lower_bound = pivot_1

    for i in l:
        if upper_bound > i > lower_bound:
            l_between.append(i)
        elif lower_bound > i:
            l_small.append(i)
        elif upper_bound < i:
            l_big.append(i)

    if k <= len(l_big):
        res = quickselect_twopivot(l_big, k, count + 1)
        return res
    elif k > len(l_big) + len(l_between) + 2:
        res = quickselect_twopivot(l_small, k - (len(l_big) + len(l_between) + 2), count + 1)
        return res
    elif len(l_big) + len(l_between) + 2 > k > len(l_big) + 1:
        res = quickselect_twopivot(l_between, k - (len(l_big) + 1), count + 1)
        return res
    else:
        if k == 1:
            return upper_bound, count
        else:
            return lower_bound, count

def simulator(length, k, runs):
    sum_onepivot = 0
    sum_twopivot = 0

    for i in range(0, runs):
        x = quickselect_onepivot(length, k, 1)
        y = quickselect_twopivot(length, k, 1)
        sum_onepivot += x[1]
        sum_twopivot += y[1]

    avg_onepivot = sum_onepivot / runs
    avg_twopivot = sum_twopivot / runs
    print("Average recursive calls for single pivot: ", avg_onepivot)
    print("Average recursive calls for double pivot: ", avg_twopivot)

test = []
while len(test) <= 150:
    i = random.randint(0, 20000)
    if i not in test:
        test.append(i)
simulator(test, 50, 30000)
