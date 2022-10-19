
#class Solution:
def romanToInt(s):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, exception, i, j = 0, 0, 0, 0

    while i < len(s):
        if s[i] == 'I':
            total += 1
        elif s[i] == 'V':
            total += 5
        elif s[i] == 'X':
            total += 10
        elif s[i] == 'L':
            total += 50
        elif s[i] == 'C':
            total += 100
        elif s[i] == 'D':
            total += 500
        elif s[i] == 'M':
            total += 1000
        i += 1

    while j < len(s):
        if s[j:j+2] == 'IV' or s[j:j+2] == 'IX':
            exception -= 1
        elif s[j:j+2] == 'XL' or s[j:j+2] == 'XC':
            exception -= 10
        elif s[j:j+2] == 'CD' or s[j:j+2] == 'CM':
            exception -= 100
        j += 1

    print(total)
    print(exception)
    return (total + exception)

s = "III"
print(romanToInt(s))