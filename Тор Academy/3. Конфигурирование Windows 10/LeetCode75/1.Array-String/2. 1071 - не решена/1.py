# 1071 Greatest Common Divisor of Strings
# easy
# наивное решениене

# - не решена

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # определяем короткую строку и длинную
        min_str = str1 if len(str1) < len(str2) else str2
        max_str = str2 if len(str2) > len(str1) else str1
        if max_str + min_str != min_str + max_str:
            return ''
        i = 1
        count = 0
        while True:
            sub_str = min_str[:i]
            count = min_str.count(min_str[:i])
            if count == 1 and i != 1:
                return min_str[:i]
            i += 1


obj = Solution()
print(f'Пример 1 - {obj.gcdOfStrings("ABABAB", "ABAB")}')
print(obj.gcdOfStrings('ABCABC', 'ABC'))
print(obj.gcdOfStrings('ABC', 'ABC'))
print('Лох')