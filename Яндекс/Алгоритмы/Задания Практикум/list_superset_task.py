def list_superset(list_set_1, list_set_2):
    if len(list_set_1) < len(list_set_2):
        temp = list_set_2
        list_set_2 = list_set_1
        list_set_1 = temp
    list_set_3 = []
    for el in list_set_2:
        if el in list_set_1:
            list_set_3.append(el)
    if (len(list_set_1) == len(list_set_2) == len(list_set_3)):
        return 'Наборы равны.'
    elif len(list_set_3) == len(list_set_2):
        return f'Набор - {list_set_1} супермножество.'
    elif (len(list_set_1) == len(list_set_2) == len(list_set_3)):
        return 'Наборы равны.'
    else:
        return 'Супермножество не обнаружено.'


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))