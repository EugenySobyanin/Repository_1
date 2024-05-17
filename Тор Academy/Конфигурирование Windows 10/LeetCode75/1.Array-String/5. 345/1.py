# 345 Reverse Vowels of a String
# easy
# Наивное решение


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [el for el in s]
        vowels_indx = []
        vowels = 'aeiou'
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_indx.append(i)
        for i in range(len(vowels_indx)):
            s[vowels_indx[i]] = s[vowels_indx[len(vowels_indx) - (i+1)]]
        return ''.join(s)
            
    
    

obj = Solution()
test1 = 'hello'
test2 = 'leetcode'
print(obj.reverseVowels(test1))
print(obj.reverseVowels(test2))