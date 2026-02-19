# Расчет НМЦК для Транспортная безопасность Оценка уязвимости
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
price_1 = 1_380_000
price_2 = 1_380_000
price_3 = 1_500_000
price_list = [price_1, price_2, price_3]

# Вывод полученных результатов
print(find_variation_coef(price_list))