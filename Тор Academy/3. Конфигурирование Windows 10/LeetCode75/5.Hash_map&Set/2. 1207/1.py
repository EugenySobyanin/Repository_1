# 1207. Unique Number of Occurrences
# easy
# наивное решение
# решено: Скорость 5%, память 78%



from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for el in arr:
            dictionary[arr.count(el)] = el
        if len(arr) != sum([el for el in dictionary]):
            return False
        return True

         
obj =  Solution()
print(obj.uniqueOccurrences([1,2,2,1,1,3]))             # true
print(obj.uniqueOccurrences([1,2]))                     # false
print(obj.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true


