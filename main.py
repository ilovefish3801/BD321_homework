if __name__ == "__main__":

    # Task 1

    # list = {
    #     'day1': {
    #         "Понеділок": "1",
    #     },
    #     'day2': {
    #         "Вівторок": "2",
    #     },
    #     'day3': {
    #         "Середа": "3",
    #     },
    #     'day4': {
    #         "Четвер": "4",
    #     },
    #     'day5': {
    #         "П'ятниця": "5",
    #     },
    #     'day6': {
    #         "Субота": "6",
    #     },
    #     'day7': {
    #         "Неділя": "7",
    #     },
    # }
    #
    # question = str(input("Введіть номер дня тижня: "))
    #
    # for i in list:
    #     for a in list[i]:
    #         if question == list[i][a]:
    #             print(a)

    # Task 2

    # list = {
    #     'month1': {
    #         "Січень": "1",
    #     },
    #     'month2': {
    #         "Лютий": "2",
    #     },
    #     'month3': {
    #         "Березень": "3",
    #     },
    #     'month4': {
    #         "Квітень": "4",
    #     },
    #     'month5': {
    #         "Травень": "5",
    #     },
    #     'month6': {
    #         "Червень": "6",
    #     },
    #     'month7': {
    #         "Липень": "7",
    #     },
    #     'month8': {
    #         "Серпень": "8",
    #     },
    #     'month9': {
    #         "Вересень": "9",
    #     },
    #     'month10': {
    #         "Жовтень": "10",
    #     },
    #     'month11': {
    #         "Листопад": "11",
    #     },
    #     'month12': {
    #         "Грудень": "12",
    #     },
    #
    # }
    #
    # question = input("Введіть номер місяця: ")
    #
    #
    # for i in list:
    #     for a in list[i]:
    #         if question == list[i][a]:
    #             print(a)

    # Task 3

    # number = int(input("Введіть число: "))
    #
    # if number > 0:
    #     print("Number is positive")
    # elif number == 0:
    #     print("Number is equal to zero")
    # else:
    #     print("Number is negative")

    # Task 4

    # numOne = int(input("Введіть перше число: "))
    # numTwo = int(input("Введіть друге число: "))
    #
    #
    # if numOne == numTwo:
    #     print("Рівні")
    # if numOne > numTwo:
    #     print(numTwo, numOne)
    # else:
    #     print(numOne, numTwo)

    # Task 5

    products = {
        'яблука': 10,
        'банани': 15,
        'апельсини': 12,
        'груші': 8,
        'киві': 20
    }

    balance = 100

    shopping_cart = []

    shopping_Cost = 0

    while balance > 0:
        for product, productPrice in products.items():
            print(product, "-", productPrice)

        productCount = int(input("Введіть кількість продуктів: "))
        productChoice = input("Введіть продукт для покупки: ")

        if productChoice == "q":
            break

        productChoice = productChoice.lower()

        if productChoice in products and productCount < 2:
            print("Товар додано до кошика")
            balance = balance - products[productChoice]
            shopping_cart.append(productChoice)
            shopping_Cost = shopping_Cost + products[productChoice]

        if productChoice not in products:
            print("\nТовар не знайдено\n")

        if productChoice in products and balance < products[productChoice]:
            print("Недостатньо коштів на рахунку")

        if productChoice in products and productCount > 1:
            balance = balance - products[productChoice] * productCount
            shopping_cart.append(f"{productChoice} Кількість: {str(productCount)})")
            shopping_Cost = shopping_Cost + products[productChoice] * productCount

        if balance == 0:
            print("\nВи витратили всі гроші\n")
            break
        elif balance < 0:
            print("\nВи будете винні нам гроші !\n")
            break

    print("Покупки: ", shopping_cart)
    print("Баланс: ", balance)
    print("Загалом потрачено грошей: ", shopping_Cost)
