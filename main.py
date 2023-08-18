if __name__ == "__main__":
    # Task 1
    # numberOne = int(input("Введіть перше число: "))
    # numberTwo = int(input("Введіть друге число: "))
    #
    # finalNum = 1
    # for i in range(numberTwo):
    #     finalNum *= numberOne
    # print(finalNum)

    # Task 2

    # count = 0
    #
    # for i in range(100, 1000):
    #     i = str(i)
    #     if i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
    #         count += 1
    # print(count)

    # Task 3

    # count = 0
    # for i in range(100, 10000):
    #     check = set(str(i))
    #     if len(check) == len(str(i)):
    #         count += 1
    # print(count)

    # count = 0
    # for i in range(100, 10000):
    #     check = {*str(i)}
    #     if len(check) == len(str(i)):
    #         count += 1
    # print(count)

    # Task 4

    number = int(input("Введіть число: "))
    number = str(number)

    newNum = ""

    for i in number:
        if i != "6" and i != "3":
            newNum += i

    print(newNum)
