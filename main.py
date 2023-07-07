if __name__ == "__main__":
    # Task 1
    # print(" ""Множення -1 \n", "Додавання -2")
    #
    # type = int(input("Введіть тип дії: "))
    #
    # num1 = int(input("Введіть перше число: "))
    # num2 = int(input("Введіть друге число: "))
    # num3 = int(input("Введіть третє число: "))
    #
    # num_Sum = num3 + num2 + num1
    # num_Product = num3 * num2 * num1
    #
    # if type == 1:
    #     print("Добуток цих чисел: ", num_Product)
    # else:
    #     print("Сума цих чисел: ", num_Sum)

    # Task 2

    # print(" ""Максимальне число -1 \n", "Мінімальне число -2 \n", "Середньоарифметичне чисел -3")
    #
    # type = int(input("Введіть тип дії: "))
    #
    # num1 = int(input("Введіть перше число: "))
    # num2 = int(input("Введіть друге число: "))
    # num3 = int(input("Введіть третє число: "))
    #
    # if type == 1:
    #     if num1 > num2 and num3:
    #         print(num1)
    #     elif num2 > num1 and num3:
    #         print(num2)
    #     else:
    #         print(num3)
    #
    # if type == 2:
    #     if num1 < num2 and num3:
    #         print(num1)
    #     elif num2 < num1 and num3:
    #         print(num2)
    #     else:
    #         print(num3)
    #
    # if type == 3:
    #     print(round((num1 + num2 + num3) / 3, 1))


    # Task 3

    print(" ""В милі -1 \n", "В дюйми -2 \n", "В ярди -3")

    type = int(input("Введіть в що перетворити: "))

    meters = int(input("Введіть кількість метрів: "))

    if type == 1:
        print("В милях: ", round(meters * 0.00062137, 2))
    elif type == 2:
        print("В дюймах: ", round(meters * 39.370, 2))
    else:
        print("В ярдах: ", round(meters * 1.0936, 2))