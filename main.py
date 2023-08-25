import random

if __name__ == "__main__":
    # Task 1
    # number = input("Введіть вираз: ")
    #
    # if '+' in number:
    #     result = number.split('+')
    #     print(int(result[0]) + int(result[1]))
    # elif '-' in number:
    #     result = number.split('-')
    #     print(int(result[0]) - int(result[1]))
    # elif '*' in number:
    #     result = number.split('*')
    #     print(int(result[0]) * int(result[1]))
    # else:
    #     result = number.split('/')
    #     print(int(result[0]) / int(result[1]))

    # Task 2
    arr = []
    for i in range(9):
        arr.append(random.randint(-100, 100))

    zeroCount = 0
    negativeCount = 0
    positiveCount = 0
    for i in arr:
        if i < 0:
            negativeCount += 1
        elif i > 0:
            positiveCount += 1
        else:
            zeroCount += 1
    print(f"Список заповненмй випадковими числами: {arr}\n")
    print(f"Максимальний елемент у списку: {max(arr)}")
    print(f"Мінімальний елемет у списку: {min(arr)}")
    print(f"Кількість від'ємних чисел у списку: {negativeCount}")
    print(f"Кількість додатніх чисел у списку: {positiveCount}")
    print(f"Кількість нулів: {zeroCount}")