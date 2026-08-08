# 345 Reverse Vowels of a String
# easy
# Заимствованное решение - 12 поскорости, 86 по памяти
# Достаточно простое решение и ПОНЯТНОЕ, которое использует метод two pointers


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        word = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if VOWELS.count(word[left]) and VOWELS.count(word[right]):
                temp = word[left]
                word[left] = word[right]
                word[right] = temp
                left += 1
                right -= 1
            elif not VOWELS.count(word[left]):
                left += 1
            else:
                right -= 1

        return "".join(word)
    

obj = Solution()
test1 = 'hello'
test2 = 'leetcode'
print(obj.reverseVowels(test1))
print(obj.reverseVowels(test2))
print(obj.reverseVowels('hoolee'))
print(obj.reverseVowels("Aa"))