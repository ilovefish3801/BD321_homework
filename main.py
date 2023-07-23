import math

import json


def taskOne():
    text1 = "Don't compare yourself with anyone in this world…"
    text2 = "if you do so, you are insulting yourself."
    print(f'"{text1}\n {text2}"\n Bill Gates')


def taskTwo(numOne, numTwo):
    for i in range(numOne, numTwo + 1, 1):
        if i % 2 == 0:
            print(i)


def taskThree(length, symbol, full):
    empty = " "
    repeat = length - 4
    if full:
        for i in range(length):
            print(symbol * length)
    else:
        for i in range(1, length + 1, 1):
            if i == 1:
                print(symbol * length)
        for a in range(3, length + 1, 1):
            print(symbol, empty * repeat, symbol)
        print(symbol * length)


def taskFour(numOne, numTwo, numThree, numFour, numFive):
    return min(numOne, numTwo, numThree, numFour, numFive)


def taskFive(numOne, numTwo):
    numcopy = numOne
    if numOne > numTwo:
        numOne = numTwo
        numTwo = numcopy

    product = 1
    for i in range(numOne, numTwo + 1, 1):
        product *= i

    print("Добуток діапазону: ", product)


def taskSix(number):
    amount = str(number)
    print("Кількість: ", len(amount))


def taskSeven(number):
    strNum = str(number)
    output = bool
    if strNum == strNum[::-1]:
        output = True
    else:
        output = False
    return output


def listSquare(customList):
    newList = []
    for i in customList:
        newList.append(math.sqrt(i))
    return newList


def factorial(n):
    numFactorial = n
    while n > 1:
        n -= 1
        numFactorial = numFactorial * n

    return numFactorial


def isPolindrom(text):
    reversedText = text[::-1]
    if text == reversedText:
        return True
    else:
        return False


def cesarCode(txt, key=3):
    with open("alphabet.json", 'r') as file:
        alphabet_data = json.load(file)
    code_in_num = []
    for letter in txt:
        for l in alphabet_data:
            if alphabet_data[f"{l}"] == letter.lower():
                code_in_num.append(int(l) + int(key))
    code_word = ''
    for num in code_in_num:
        if num <= 26:
            code_word += alphabet_data[f"{num}"]
        else:
            code_word += alphabet_data[f"{num - 26}"]
    return code_word.capitalize()


def romanNumbers(number):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    arabicNumbers = 0
    output = 0

    for i in reversed(number):
        sum = roman_numerals[i]
        if sum >= output:
            arabicNumbers += sum
        else:
            arabicNumbers -= sum
        output = sum

    return arabicNumbers


def amountWords(words):
    splited = words.split()
    return len(splited)


# Формула простих чисел невідома тому не напишу функцію )

def polishCalculator(numbers):
    whatToDo = numbers.split()
    actions = ["+", "*", "-", "/"]
    action = whatToDo[0]
    numOne = int(whatToDo[1])
    numTwo = int(whatToDo[2])
    result = 0

    if actions[0] == action:
        return numOne + numTwo
    if actions[1] == action:
        return numOne * numTwo
    if actions[2] == action:
        return numOne - numTwo
    else:
        return numOne / numTwo


def listMerge(listOne, listTwo):
    newList = []
    for i in listOne:
        for a in listTwo:
            if i == a:
                newList.append(i)
    return newList


if __name__ == "__main__":
    taskOne()

    taskTwo(1, 10)

    taskThree(5, "*", True)

    print(taskFour(49, 50, 3, 1, 67))

    taskFive(1, 5)

    taskSix(351452)
    
    print(taskSeven(121))

    print(listSquare([4, 16]))

    print(factorial(4))

    print(isPolindrom("aba"))

    print(cesarCode("python"))

    print(romanNumbers("IX"))

    print(amountWords("hello world"))

    print(polishCalculator("* 8 3"))

    print(listMerge([1, "a", 5], [3, 1, 6, 5]))
