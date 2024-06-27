# 151. Reverse Words in a String
# medium
# Заимствованное решение - 49 по скорости, 9 по памяти
# более элегантное решение


class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()[::-1]
        reverse_string = " ".join(string)
        return reverse_string


obj = Solution()
print(obj.reverseWords('Раз два три'))
print(obj.reverseWords('Белый  Синий    Красный'))
print(obj.reverseWords('Всем привет, меня зовут Олег!'))