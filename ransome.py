
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for i in ransomNote:
            if i in letters:
                if letters[i] == 0:
                    return False
                letters[i] -= 1
            else:
                return False
        return True

