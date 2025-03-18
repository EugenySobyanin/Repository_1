# Расчет НМЦК для пресса лаборатории

from math import sqrt


def find_variation_coef(coasts: list) -> str:
    """"Расчет коэф.вариации и средней цены на основании списка с коммерческими предложениями."""
    AVG_coast = round(sum(coasts) / len(coasts), 2)
    standard_deviation = 0
    for i in range(len(coasts)):
        standard_deviation += (coasts[i] - AVG_coast)**2
    print(f'Сумма квадратичных отклонений= {standard_deviation}')
    standard_deviation = round(sqrt(standard_deviation / (len(coasts) - 1)), 4)
    variation_coef = round(standard_deviation * 100 / AVG_coast, 2)
    return (
        (f'Средняя цена= {AVG_coast}\n'
         f'Среднеквадратическое отклоненеие {standard_deviation}\n'
         f'Коэф. вариации= {variation_coef}\n'
         ))


# входные данные
price_list = [2_440_160.00, 2_401_633.00, 2_361_700.00]

# Вывод полученных результатов
print(find_variation_coef(price_list))