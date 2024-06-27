# 151. Reverse Words in a String
# medium
# Переделал решение 2 в одну строку - 91 по скорости, 32 по памяти
# Решение 2 в одну строку


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


obj = Solution()
print(obj.reverseWords('Раз два три'))
print(obj.reverseWords('Белый  Синий    Красный'))
print(obj.reverseWords('Всем привет, меня зовут Олег!'))