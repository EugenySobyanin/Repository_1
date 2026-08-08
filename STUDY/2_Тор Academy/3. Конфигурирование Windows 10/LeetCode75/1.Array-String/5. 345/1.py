# 345 Reverse Vowels of a String
# easy
# Наивное решение
# Решено - 68 поскорости, 14 по памяти


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [el for el in s]
        vowels_indx = []
        vowels = 'aeiou'
        # Если гласная буква то добавляем ее индекс в vowels_indx
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowels_indx.append(i)

        # Проходим список с индексами гласных в строке s
        for i in range(int(len(vowels_indx) / 2)):
            left = vowels_indx[i]
            right = vowels_indx[len(vowels_indx) - (i+1)]
            s[left], s[right] = s[right], s[left]
        return ''.join(s)


obj = Solution()
test1 = 'hello'
test2 = 'leetcode'
print(obj.reverseVowels(test1))
print(obj.reverseVowels(test2))
print(obj.reverseVowels('hoolee'))
print(obj.reverseVowels("Aa"))