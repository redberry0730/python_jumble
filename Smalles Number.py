


# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n + 1 is created using the following conditions:
# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = ""
        s = []
        n = 1
        for i in range(len(pattern)):
            s.append(n)
            n += 1
            if pattern[i] != "D":
                while s:
                    result += str(s.pop())
        s.append(n)
        while s:
            result += str(s.pop())
        return result