# Задача отсортировать колоду карт (52) по масти и по старшинству

from random import choice

# созданипе и заполнение массива с картами
SUIT_COUNT = 13
CARDS_COUNT = SUIT_COUNT * 4

arr = [None] * CARDS_COUNT
suits = ['a', 'b', 'c', 'd']
suit_counts = {
    'a': SUIT_COUNT,
    'b': SUIT_COUNT,
    'c': SUIT_COUNT,
    'd': SUIT_COUNT
}

for i in range(CARDS_COUNT):
    for key, value in suit_counts.items():
        if value == 0 and key in suits:
            suits.remove(key)
    arr[i] = choice(suits)
    suit_counts[arr[i]] -= 1

print(f'Массив перед сортировкой:\n {arr}')

# Сортировка по масти
for i in range(0, len(arr), SUIT_COUNT):
    count = 1
    suit = arr[i]
    card_to_change = i + 1
    for j in range(i + 1, len(arr)):
        if arr[j] == suit:
            arr[j], arr[card_to_change] = arr[card_to_change], arr[j]
            count += 1
            card_to_change += 1

        if count == SUIT_COUNT:
            break

print(f'Массив после сортировки:\n {arr}')
