# Задача 2. Написать функцию/метод, которая на вход получает
# массив положительных целых чисел произвольной длины.
# Например [42, 12, 18]. На выходе возвращает массив чисел,
# которые являются общими делителями для всех указанных числе.
# В примере это будет [2, 3, 6].


def getDividers(numbers: [int]) -> [int]:
    dividers = []
    isDivider = True
    for divider in range(2, min(numbers) + 1):
        for number in numbers:
            if number % divider != 0:
                isDivider = False
        if isDivider:
            dividers.append(divider)
        isDivider = True


    return dividers


print(getDividers([42, 12, 18]))
