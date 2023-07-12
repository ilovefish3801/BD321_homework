import json

if __name__ == "__main__":
# # Task 1

#  # Користувач вводить числа діапазону
# num_One = int(input("Введіть початок діапазону: "))
# num_Two = int(input("Введіть кінець діапазону: "))
#
# # Визначаємо діапазон
# for i in range(num_One, num_Two + 1, 1):
#     # Виводимо числа кратні 7 на екран
#     if i % 7 == 0:
#         print("Число кратне 7 у діапазоні: ", i)

# Task 2

# # Користувач вводить числа діапазону
# num_One = int(input("Введіть початок діапазону: "))
# num_Two = int(input("Введіть кінець діапазону: "))
#
#
#
# # Визначаємо діапазон
# for i in range(num_One, num_Two + 1, 1):
#     # Виводимо всі числа діапазону
#     print(i)
#
# print("\nПеревернутий діапазон: \n")
#
# # Виводимо перевернутий діапазон
# for i in range(num_Two, num_One - 1, -1):
#     print(i)
#
#
# num = 0
# for i in range(num_One, num_Two + 1, 1):
#     # Виводимо числа кратні 7
#     if i % 7 == 0:
#         print("\n")
#         print("Число кратне 7: ", i)
#     # Знаходимо кількість чисел кратних 5
#     if i % 5 == 0:
#         num += 1
# # Виводимо кількість чисел кратних 5
# print("\n")
# print("Чисел кратних 5: ", num)

# Task 3
# # Вводимо данні
# num_One = int(input("Введіть початок діапазону: "))
# num_Two = int(input("Введіть кінець діапазону: "))
#   # # Робимо діапазон
# for i in range(num_One, num_Two + 1, 1):
# # Якщо число кратне 3 і 5 виводимо Fizz Buzz
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz Buzz")
# # Якщо число кратне 3  виводимо Fizz
#         elif i % 3 == 0:
#         print("Fizz")
# # Якщо число кратне  5 виводимо  Buzz
#     elif i % 5 == 0:
#         print("Buzz")
# # Виводимо решту чисел
#     else:
#         print(i)

# Task 4
# # Вводимо id елемента щоб видалити
# id_choice = int(input("Введіть id для видалення: "))
#
# # Відкриваємо json
# with open("products.json", "r") as file:
#     products = json.load(file)
#
# # Берем index та сам лист
# for index, list in enumerate(products):
# # Якщо id введене = id яке є у листі то видалити index в якому воно знаходиться
#     if list['id'] == id_choice:
#         products.pop(index)
#
# # Видаляємо index того id
# with open("products.json", "w") as file:
#     json.dump(products, file)
