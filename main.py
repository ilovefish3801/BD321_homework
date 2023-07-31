def taskTwo1(name, age):
    if 0 < age < 130:
        return f"Привіт, {name.title()}! Твій вік — {age}"
    else:
        return "Ви не добре ввели вік"


def taskTwo2(name, age):
    try:

        if 0 < age < 130:
            return f"Привіт, {name.title()}! Твій вік — {age}"
        else:
            return "Ви не добре ввели вік"

    except Exception as err:
        return f"Виникла помилка: {err}"


def taskThree1(list):
    result = 0
    for i in list:
        result += i
        if result < 0:
            return "\nВи ввели від'ємне число "
            break

    return result

def taskThree2(list):
    try:
        result = 0
        for i in list:
            result += i
            if result < 0:
                return "\nВи ввели від'ємне число "
                break

        return result
    except Exception as err:

        print(f"Виникла помилка {err}")
if __name__ == "__main__":
    # Input для 1 та 2 завдання
    # name = input("Введіть ім'я: ")
    # name = name.lower()
    # age = int(input("Введіть свій вік: "))

    # Task 1
    # try:
    #     if 0 < age < 130:
    #         print(f"Привіт, {name.title()}! Твій вік — {age}")
    #     else:
    #         print("Ви не добре ввели вік")
    # except Exception as err:
    #     print(f"Виникла помилка: {err}")

    # Task 2, method 1

    # try:
    #     print(taskTwo1(name, age))
    # except Exception as err:
    #     print(f"Виникла помилка: {err}")

    # Task 2, method 2
    # print(taskTwo2(name, age))

    # Task 3
    # arr = []
    # result = 0
    #
    # flag = True
    # while flag:
    #     print("\nЩоб вийти та побачити результат напишіть 0")
    #     number = int(input("Введіть число, щоб додати: "))
    #
    #     if number != 0:
    #         arr.append(number)
    #
    #     if number == 0:
    #
    #         flag = False
    #         try:
    #             for i in arr:
    #                 result += i
    #
    #                 if result < 0:
    #                     print("\nВи ввели від'ємне число ")
    #                     break
    #                 else:
    #                     print(result)
    #
    #
    #         except Exception as err:

    # Task 4 method 1

    # try:
    #     print(taskThree1([0, 2, 3]))
    # except Exception as err:
    #     print(f"Виникла помилка {err}")

    # task 4 method 2

    print(taskThree2([1, 2, 3]))