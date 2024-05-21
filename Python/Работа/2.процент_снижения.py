
max_coast = 25_094_945.28

declines = [60.15, 58, 17.10, 56.17, 28.27, 0, 0, 0.02]


def get_result_costs(declines):
    results = []
    i = 0
    for el in declines:
        results.append(max_coast - (max_coast * el / 100))
        print(f'{i + 1} место - {round(results[i], 2)}')
        i += 1

get_result_costs(declines)
