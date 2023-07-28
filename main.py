def taskOne(list):
    product = 1
    for i in list:
        product = product * i
    return product


def taskTwo(list):
    return min(list)


# 3 завдання не знаю чи можна зробити ви казали, що формули простих чисел немає але якщо рішення є скажіть його будь ласка

def taskFour(list, delNumber):
    try:
        delnumIndex = list.index(delNumber)
    except Exception as err:
        return "Ви вибрали число якого немає в списку"

    list.pop(delnumIndex)
    return list


def taskFive(listOne, listTwo):
    mergedList = []
    for i in listOne:
        for a in listTwo:
            if i == a:
                mergedList.append(a)

    return mergedList


def taskSix(list, degree):
    finishedList = []
    for i in list:
        i = i ** degree
        finishedList.append(i)
    return finishedList


if __name__ == "__main__":
    