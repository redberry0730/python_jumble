import random
import math

def gsr(l):
    sequence = []
    heads = 0
    tails = 0

    i = 0
    while i < len(l):
        flip_result = random.randint(0, 1)
        if flip_result == 1:
            heads += 1
        else:
            tails += 1
        sequence.append(flip_result)
        i += 1

    left_side = []
    right_side = []
    for j in range(0, heads):
        left_side.append(l[j])

    for k in range(0, tails):
        right_side.append(l[heads + k])

    result = []
    pointer1 = 0
    pointer2 = 0
    for num in sequence:
        if num == 1:
            result.append(left_side[pointer1])
            pointer1 += 1
        else:
            result.append(right_side[pointer2])
            pointer2 += 1

    return result

def top_to_random(l):
    placing = random.randint(0, len(l)-1)
    result = l.copy()
    top_card = result[0]
    result.pop(0)
    result.insert(placing, top_card)
    return result

def test_order(i, j, l):
    for x in l:
        if x == i:
            return True
        elif x == j:
            return False

def num_trials(err, prob):
    return math.ceil(0.25 / (math.pow(err, 2) * prob))

def gsr_order_prob(n, k, i, j, err, prob):
    total_trials = num_trials(err, prob)
    whole_deck = []
    for h in range(0, n):
        whole_deck.append(h)

    current_trial = 0
    count = 0
    while current_trial < total_trials:
        copied_deck = whole_deck.copy()
        for sky in range(0, k):
            copied_deck = gsr(copied_deck)
        if test_order(i, j, copied_deck):
            count += 1
        current_trial += 1

    probability = count / total_trials
    return probability

def top_to_random_order_prob(n, k, i, j, err, prob):
    total_trials = num_trials(err, prob)
    whole_deck = []
    for h in range(0, n):
        whole_deck.append(h)

    current_trial = 0
    count = 0
    while current_trial < total_trials:
        copied_deck = whole_deck.copy()
        for sky in range(0, k):
            copied_deck = top_to_random(copied_deck)
        if test_order(i, j, copied_deck):
            count += 1
        current_trial += 1

    probability = count / total_trials
    return probability