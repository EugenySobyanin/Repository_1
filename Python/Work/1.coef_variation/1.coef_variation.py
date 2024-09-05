from math import sqrt


# coast1 = 2_900_000
# coast2 = 2_788_585
# coast3 = 2_936_958.80
# coasts_count = 3

# AVG_coast = round((coast1 + coast2 + coast3) / coasts_count, 2)


# standard_deviation = round(sqrt(((coast1 - AVG_coast)**2 + (coast2 - AVG_coast)**2 + (coast3 - AVG_coast)**2) / (coasts_count - 1)), 2)

# variation_coef = round(standard_deviation * 100 / AVG_coast, 2)


# print(AVG_coast)
# print(standard_deviation)
# print(variation_coef)


def find_variation_coef(coasts: list) -> tuple[str, float]:
    """"Расчет коэф.вариации и средней цены на основании списка с коммерческими предложениями."""
    AVG_coast = round(sum(coasts) / len(coasts), 2)
    standard_deviation = 0
    for i in range(len(coasts)):
        standard_deviation += (coasts[i] - AVG_coast)**2
    # print(f'Сумма квадратичных отклонений= {standard_deviation}')
    standard_deviation = round(sqrt(standard_deviation / (len(coasts) - 1)), 4)
    variation_coef = round(standard_deviation * 100 / AVG_coast, 2)
    return (
        (f'Средняя цена= {AVG_coast}\n'
         f'Среднеквадратическое отклоненеие {standard_deviation}\n'
         f'Коэф. вариации= {variation_coef}\n'
         ),
        AVG_coast)


# Входные данные
hranitel_ptd = [3_544_200.00, 3_544_200.00, 2_801_700.00, 9_839_300.00, 3_544_200.00]
vostok = [3_705_176.00, 3_690_176.00, 2_947_886.00, 10_207_164.00, 3_691_176.00]
nadezhny = [3_728_264.00, 3_714_264.00, 2_966_804.00, 10_260_056.00, 3_714_264.00]

obj1 = [hranitel_ptd[0], vostok[0], nadezhny[0]]
obj2 = [hranitel_ptd[1], vostok[1], nadezhny[1]]
obj3 = [hranitel_ptd[2], vostok[2], nadezhny[2]]
obj4 = [hranitel_ptd[3], vostok[3], nadezhny[3]]
obj5 = [hranitel_ptd[4], vostok[4], nadezhny[4]]

# print(f'Хранитель-ПТБ: {hranitel_ptd:,}'.replace(',', ' '))
# print(f'Восток       : {vostok:,}'.replace(',', ' '))
# print(f'Надежный     : {nadezhny:,}\n'.replace(',', ' '))

# Вызов функции для расчета
# print(find_variation_coef([sum(hranitel_ptd), sum(vostok), sum(nadezhny)])[0])

result = 0
for i, el in enumerate([obj1, obj2, obj3, obj4, obj5]):
    avg = find_variation_coef(el)[1]
    print(f'obj{i+1} - {avg}')
    result += avg
    
print(f'Сумма: {result}')