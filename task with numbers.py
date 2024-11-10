# Задача 2. Есть числа от трех до одиннадцати. Есть квадрат — 3 на 3 клетки:
# а б в
# г д е
# ё ж з
# (Буквы ничего не значат, кроме того, что числа не повторяются)
# Можно ли расставить числа в клетки квадрата таким образом,
#  что перемножения чисел в строках дает тот же результат,
#  что и произведение чисел в столбцах с теми же номерами?
# Если можно — расставьте, если нельзя — объясните почему.


import random

originalNumbers = [3,4,5,6,7,8,9,10,11]

row1 = []
row2 = []
row3 = []

find = False


def generateMatrix():
    numbers = originalNumbers.copy()
    random.shuffle(numbers)
    # print(numbers)
    global row1
    row1 = numbers[:3]
    global row2
    row2 = numbers[3:6]
    global row3
    row3 = numbers[6:]



def rowMultiplication(numbers) -> int:
    result = 1
    for i in numbers:
        result *= i
    return result


generateMatrix()
iterations = 0
while not find:
    if (rowMultiplication(row1) == (row1[0]*row2[0]*row3[0])) and (rowMultiplication(row2) == (row1[1]*row2[1]*row3[1])) and (rowMultiplication(row3) == (row1[2]*row2[2]*row3[2])):
        print("#######################")
        print(row1)
        print(row2)
        print(row3)
        print("УРА!!!")
        print("#######################")
        find = True
    else:
        generateMatrix()
        iterations += 1
        print(f'iterations = {iterations}')
