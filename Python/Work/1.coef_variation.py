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


def find_variation_coef(coasts: list):
    """"Расчет коэф.вариации и средней цены на основании списка с коммерческими предложениями."""
    AVG_coast = round(sum(coasts) / len(coasts), 2)
    standard_deviation = 0
    for i in range(len(coasts)):
        standard_deviation += (coasts[i] - AVG_coast)**2
    print(f'Сумма квадратичных отклонений= {standard_deviation}')
    standard_deviation = round(sqrt(standard_deviation / (len(coasts) - 1)), 4)
    variation_coef = round(standard_deviation * 100 / AVG_coast, 2)
    return (f'Средняя цена= {AVG_coast}\n'
            f'Среднеквадратическое отклоненеие {standard_deviation}\n'
            f'Коэф. вариации= {variation_coef}\n'
            )

# Входные данные
hranitel_ptd = sum([3_544_200.00, 3_544_200.00, 2_801_700.00, 9_839_300.00, 3_544_200.00])
vostok = sum([3_705_176.00, 3_690_176.00, 2_947_886.00, 10_207_164.00, 3_691_176.00])
nadezhny = sum([3_728_264.00, 3_714_264.00, 2_966_804.00, 10_260_056.00, 3_714_264.00])

print(f'Хранитель-ПТБ: {hranitel_ptd:,}'.replace(',', ' '))
print(f'Восток       : {vostok:,}'.replace(',', ' '))
print(f'Надежный     : {nadezhny:,}\n'.replace(',', ' '))

# Вызов функции для расчета
print(find_variation_coef([hranitel_ptd, vostok, nadezhny]))

