# 605. Can Place Flowers
# easy
# наивное решение не проходило
# подсмотрена идея c добавление в начало и конец нулей


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # добавляем нули в конец и в начало списка
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        for i in range(1, len(flowerbed) - 1):
            if count >= n:
                return True
            # смотрим текущий, предыдущий, последующий элементы
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                # меняем текущий эл.т на 1
                flowerbed[i] = 1
            if count >= n:
                return True
        return False


obj = Solution()
test1 = ([1, 0, 0, 0, 1], 1)
test2 = ([1, 0, 0, 0, 1], 2)
test3 = ([0, 0, 1, 1, 1, 1, 0, 0, 0, 1], 2)


print(obj.canPlaceFlowers(*test1))
print(obj.canPlaceFlowers(*test2))
print(obj.canPlaceFlowers(*test3))