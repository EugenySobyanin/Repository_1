# 345 Reverse Vowels of a String
# easy
# Заимствованное решение - 80 поскорости, 53 по памяти
# Эффектное решение, хорошо по скорости и по памяти


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r, s = 0, len(s)-1, list(s)
        vowels = 'aeiouAEIOU'

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l += s[l] not in vowels # инкремент через условие, очень эффектно!!!
            r -= s[r] not in vowels

        return "".join(s)
    

obj = Solution()
test1 = 'hello'
test2 = 'leetcode'
print(obj.reverseVowels(test1))
print(obj.reverseVowels(test2))
print(obj.reverseVowels('hoolee'))
print(obj.reverseVowels("Aa"))