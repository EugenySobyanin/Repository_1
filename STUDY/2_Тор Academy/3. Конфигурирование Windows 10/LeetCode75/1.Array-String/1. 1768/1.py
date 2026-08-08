# 1768. Merge Strings Alternately 
# easy
# решено
# первое мое самостоятельное решение

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        word_1_2 = word1
        word_2_2 = word2
    
        for i in range(min(len(word1), len(word2))):
            result += word1[i]
            # После добавления i - ог эл.та, удаляем перый символ у скопированной строки
            word_1_2 = word_1_2[1:]
            result += word2[i]
            word_2_2 = word_2_2[1:]
    
        reminder = word_2_2 if word_1_2 == '' else word_1_2
        return result + reminder