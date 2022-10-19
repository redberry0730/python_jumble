

# s = '12:01:00PM'
# #s = list(s)
#
# if "P" in s:
#     if int(s[:2]) != 12:
#         s = str(int(s[:2]) + 12) + s[2:-2]
# else:
#     if int(s[:2]) == 12:
#         s = '00' + s[2:-2]
#
# print(s)


def breakingRecords(scores):
    mini, maxi = 0, 0
    pointer1, pointer2 = scores[0], scores[0]
    for i in range(len(scores)):
        if scores[i] > pointer1:
            maxi += 1
            pointer1 = scores[i]
        elif scores[i] < pointer2:
            mini += 1
            pointer2 = scores[i]
    return [mini, maxi]

scores = [12, 24, 10, 24]
print(breakingRecords(scores))