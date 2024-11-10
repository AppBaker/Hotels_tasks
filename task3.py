# Задача 3. Написать функцию/метод, которая возвращает массив простых
# чисел в диапазоне (2 числа - минимальное и максимальное) заданных чисел.
# Например, на вход переданы 2 числа: от 11 до 20
# (диапазон считается включая граничные значения).
# На выходе программа должна выдать [11, 13 , 17, 19]

def getSimpleNumbers(min: int, max: int) -> [int]:
    simpleNums = []
    dividerCount = 0
    for number in range(min, max+1):
        for divider in range(1, number + 1):
            if number % divider == 0:
                dividerCount += 1
        if dividerCount <3:
            simpleNums.append(number)
        dividerCount = 0
    return simpleNums


print(getSimpleNumbers(11,20))