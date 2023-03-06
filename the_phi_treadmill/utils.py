from math import trunc


def trunc_to_n_decimals(list, n=1):
    for i in list:
        yield trunc(i * 10 ** n) / 10 ** n


def round_to_even_values(list, decimals=1):
    for elem in list:
        yield elem if (elem * 10 ** decimals) % 2 == 0 \
            else round(elem + 1 / 10 ** decimals, decimals)


def merge_3(list1, list2, list3):
    i = 0
    result = []
    while i < len(list1):
        result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
            result.append(list3[i])
        i += 1
    for v in result:
        yield v
