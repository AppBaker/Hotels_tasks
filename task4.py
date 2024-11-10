# Задача 4. Написать метод, который в консоль выводит таблицу умножения.
# На вход метод получает число, до которого выводит таблицу умножения.
# В консоли должна появиться таблица.


def getTableBradis(size: int):
    line = " "
    for i in range(1, size + 1):
        line += f" {i}"
    line += "\n"
    for row in range(1, size + 1):
        line += f"{row}"
        for col in range(1, size + 1):
            line += f" {col * row}"
        line += "\n"
    print(line)


getTableBradis(5)