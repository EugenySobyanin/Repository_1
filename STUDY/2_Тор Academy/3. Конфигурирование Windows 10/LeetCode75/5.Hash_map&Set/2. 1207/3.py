# 1207. Unique Number of Occurrences
# easy
# Интересное решение с применение класса Counter(подсчитывает кол.во эл.тов в последовательности)
# решено: Скорость 25%, память 6 %


from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values()))==len(Counter(arr).values())