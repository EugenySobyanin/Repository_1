# 1207. Unique Number of Occurrences
# easy
# Первое решение с генератором словарей, понтовое решение
# решено: Скорость 5%, память 99.80 %


from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return sum({arr.count(el): el for el in arr}) == len(arr)


obj =  Solution()
print(obj.uniqueOccurrences([1,2,2,1,1,3]))             # true
print(obj.uniqueOccurrences([1,2]))                     # false
print(obj.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true
