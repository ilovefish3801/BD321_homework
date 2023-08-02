# Task 2 method 1
def task2M1(number):
    faktorial = 1

    for i in range(1, number + 1):
        faktorial *= i
    return faktorial


# Task 2 method 2
def task2M2(number):
    faktorial = 1

    for i in range(1, number + 1):
        faktorial *= i

    if number > 0:
        return f"Факторіал числа {number}: {faktorial}"
    else:
        return "Ви ввели від'ємне число"


if __name__ == "__main__":
    # Task 1
    # number = int(input("Введіть число: "))
    # faktorial = 1
    #
    # for i in range(1, number + 1):
    #     faktorial *= i
    #
    # if number > 0:
    #     print(f"Факторіал числа {number}: {faktorial}")
    # else:
    #     print("Ви ввели від'ємне число")
    #
    # # Task 2 method 1
    # result = task2M1(-2)
    #
    # if result == 1 or result == None:
    #     print("Ви ввели від'ємне число")
    # else:
    #     print(f"Факторіал числа {result}")

    # Task 2 method 2

    print(task2M2(10))

    # Task 3
    # list = []
    # flag = True
    # while flag:
    #     listInput = input("Введіть числа, щоб додати (q, щоб робити операції) ")
    #     try:
    #         listInput = int(listInput)
    #     except Exception as err:
    #         listInput = str(listInput)
    #
    #     if type(listInput) == int:
    #         list.append(listInput)
    #         print("\nВи додали чосло до списку\n")
    #     elif listInput == "q":
    #         try:
    #             list[0] / 1
    #         except Exception as err:
    #             print("\nВаш лист пустий")
    #             break
    #         flag = False
    #         print(
    #             "\n 1 - Відображення списку\n 2 - Отримання максимального значення у списку\n 3 - Отримання мінімального значення у списку\n 4 - Відображення значення елемента за індексом, введеним користувачем\n 5 - Видалення елемента за індексом, введеним користувачем\n")
    #         operation = int(input("Введіть число: "))
    #         if operation == 1:
    #             print("Ось ваш список: ", list)
    #         elif operation == 2:
    #             print("Найбільше число у списку: ", max(list))
    #         elif operation == 3:
    #             print("Найменше число у списку: ", min(list))
    #         elif operation == 4:
    #             index = int(input("Введіть індекс елемента: "))
    #             try:
    #                 print(f"\nЕлемент за індекслм {index}: {list[index]}\n")
    #             except Exception as err:
    #                 print("\nВи ввели індекс якого немає")
    #                 break
    #         else:
    #             index = int(input("Введіть індекс елемента для видалення: "))
    #             try:
    #                 list.pop(index)
    #                 print(f"\nЕлемент за індексом {index} було видалено")
    #                 print(list)
    #             except Exception as err:
    #                 print("\nВи ввели індекс якого немає")
    #                 break
    #     else:
    #         print("\nВи помилково ввели щось \n")


    # Task 4 m2, m1 я не дуже розумію як це робити це треба зробити пару функцій чи через одну