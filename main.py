import math

if __name__ == "__main__":
    # # Task 1
    #
    # # Вводимо початок і кінець діапазону
    # start = int(input("Введіть початок діапазону: "))
    # finish = int(input("Введіть кінець діапазону: "))
    #
    # # Робимо сам діапазон
    # for item in range(start, finish + 1, 1):
    #     # Принтуємо тільки прості числа
    #     if item == 2:
    #         print(2)
    #     if item == 3:
    #         print(3)
    #     if item == 5:
    #         print(5)
    #     if item == 7:
    #         print(7)
    #     if item % 2 != 0 and item % 3 != 0 and item % 5 != 0 and item % 7 != 0:
    #         print(item)

    # Task 2

    # # Робимо змінну яка буде = end, щоб після кожного множення принтити з нового рядка
    # num_New = ''
    #
    # # Робимо 2 діапазони від 1 до 10 щоб зробити множення
    # for num in range(1, 10 + 1, 1):
    #     for item in range(1, 10 + 1, 1):
    #         # Робимо таблицю множення
    #         frame = f"{num} * {item} = ", num * item,
    #
    #         # Пишемо новий стовпчик з нового рядка
    #         if item == 10:
    #             num_New = '\n'
    #         else: num_New = ''
    #         # Принтимо саму таблцию
    #         print(frame, end=num_New)

    # Task 3

    # Вписуємо початок і кінець таблиці
    start = int(input("Введіть початок діапазону: "))
    finish = int(input("Введіть кінець діапазону: "))
    #  Робимо діапазон
    for num in range(start, finish + 1, 1):
        for item in range(1, 10 + 1, 1):
            # Робимо таблицю множення
            frame = f"{num} * {item} = ", num * item,
            # Пишемо новий стовпчик з нового рядка
            if item == 10:
                num_New = '\n'
            else:
                num_New = ''
            # Принтимо саму таблцию
            print(frame, end=num_New)
