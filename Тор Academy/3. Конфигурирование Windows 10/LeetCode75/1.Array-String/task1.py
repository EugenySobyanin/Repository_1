
# 1768. Merge Strings Alternately


def mergeAlternately(word1: str, word2: str) -> str:
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


if __name__ == '__main__':
    word1 = '1234'
    word2 = 'defxerox'
    print(mergeAlternately(word1, word2))

    word3 = 'ab55'
    word4 = "pq"
    print(mergeAlternately(word3, word4))

    word5 = ''
    word6 = 'href'
    print(mergeAlternately(word5, word6))
