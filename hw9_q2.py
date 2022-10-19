from scipy.special import binom

def calculator(n, k):
    probability = 0;
    type_1 = 0;

    for j in range(k, n+1):
        probability += binom(n, j) * pow(0.70, j) * pow(0.30, (n-j));
        type_1 += binom(n, j) / pow(2, n);

    type_2 = 1 - probability;

    if type_2 < 0.05 and type_1 < 0.05:
        print("n =", n, "k =", k, "Probability =", round(probability, 6),
              "Type I Error =", round(type_1, 6), "Type II Error =", round(type_2, 6));

for i in range (1, 70):
    for j in range (0, i+1):
        calculator(i, j);






