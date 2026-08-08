# 1768. Merge Strings Alternately
# easy
# мое второе решение, которое работает хуже чем первое

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        index = 0
        mini = len(min(word1, word2))
        while index != min(len(word1), len(word2)):
            result += word1[index]
            result += word2[index]
            index += 1
        result += word1[index:] if len(word1) > len(word2) else word2[index:]
        return result



obj = Solution()
word1_1 = 'abc'
word1_2 = 'pqr'
print(obj.mergeAlternately(word1_1, word1_2))

word2_1 = 'abcd'
word2_2 = 'pq'
print(obj.mergeAlternately(word2_1, word2_2))