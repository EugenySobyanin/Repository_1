# 151. Reverse Words in a String
# medium
# наивное решение
# решено - 82 по скорости, 80 по памяти


class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst_rev = []
        for i in range(len(lst) - 1, -1, -1):
            lst_rev.append(lst[i])
        return ' '.join(lst_rev)


obj = Solution()
print(obj.reverseWords('Раз два три'))
print(obj.reverseWords('Белый  Синий    Красный'))
print(obj.reverseWords('Всем привет, меня зовут Олег!'))
