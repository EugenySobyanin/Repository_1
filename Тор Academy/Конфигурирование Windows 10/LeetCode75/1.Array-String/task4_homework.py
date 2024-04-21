# 1431. Kids With the Greatest Number of Candies


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # наивное решение
        # result = []
        # maximum_el = (max(candies))
        # for el in candies:
        #     if el + extraCandies >= maximum_el:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        # Решение в одну строку
        return [True if el + extraCandies >= max(candies) else False for el in candies]  


obj = Solution()    
test1 = [2, 3, 5, 1, 3]
print(obj.kidsWithCandies(test1, 3))
