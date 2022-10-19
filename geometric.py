import random
import numpy as np

def part1_actual_formula(p, q):
    probability = (p * q) / ((p + q) - (p * q))
    return probability

def part1_simulator(p, q, size):
    x = np.random.geometric(p = p, size = size)
    y = np.random.geometric(p = q, size = size)
    equal_val = np.equal(x, y)
    count = np.count_nonzero(equal_val)
    probability = count / size
    return probability

# print("Q1 Probability given by calculation:", round(part1_actual_formula(0.25, 0.25), 5))
# print("Q1 Probability given by simulation:", round(part1_simulator(0.25, 0.25, 10000), 5))

def part2_actual_formula(p, q):
    expected_value = (1/p) + (1/q) - (1/(p + q - (p * q)))
    return expected_value

def part2_simulator(p, q, size):
    total = 0
    for i in range(0, size):
        x = np.random.geometric(p = p)
        y = np.random.geometric(p = q)
        total += max(x, y)
    expected_value = total / size
    return expected_value

# print("Q2 Expected value given by calculation:", round(part2_actual_formula(0.5, 0.5), 5))
# print("Q2 Expected value given by simulation:", round(part2_simulator(0.5, 0.5, 10000), 5))

def part3_actual_formula(p, q, k):
    probability = pow((1-p) * (1-q), k-1) * (p + q - (p * q))
    return probability

def part3_simulator(p, q, k, size):
    x = np.random.geometric(p = p, size = size)
    y = np.random.geometric(p = q, size = size)
    z = []
    count = 0
    for i in range(0, len(x)-1):
        z.append(min(x[i], y[i]))
        if z[i] == k:
            count += 1
    probability = count / size
    return probability

print("Q3 Probability given by calculation:", round(part3_actual_formula(0.5, 0.5, 2), 5))
print("Q3 Probability given by simulation:", round(part3_simulator(0.5, 0.5, 2, 10000), 5))

def part4_actual_formula(p, q):
    expected_value = 1 / (p + q - (p * q))
    return expected_value

def part4_simulator(p, q, size):
    count = 0
    total = 0
    for i in range(0, size):
        x = np.random.geometric(p = p)
        y = np.random.geometric(p = q)
        if x <= y:
            total += x
            count += 1
    expected_value = total / count
    return expected_value

print("Q4 Expected value given by calculation:", round(part4_actual_formula(0.5, 0.5), 5))
print("Q4 Expected value given by simulation:", round(part4_simulator(0.5, 0.5, 10000), 5))