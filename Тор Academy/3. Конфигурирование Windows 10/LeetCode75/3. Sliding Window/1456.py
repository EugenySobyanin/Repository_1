# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right, result, max_result = 0, k - 1, 0, 0
        vowels = 'aeiou'
        for i in range(k):
            if s[i] in vowels:
                result += 1
        max_result = result
        while right < len(s) - 1:
            left += 1
            right += 1
            result = result - 1 if s[left - 1] in vowels else result
            result = result + 1 if s[right] in vowels else result
            max_result = max(max_result, result)
        return max_result


obj = Solution()
    
test1 = ('abciiidef', 3)
test2 = ('aeiou', 2)
test3 = ('leetcode', 3)

print(obj.maxVowels(*test1))
print(obj.maxVowels(*test2))
print(obj.maxVowels(*test3))
