# Завдання 1
# Користувач зберігає печиво у спеціальному кошику.
# Потрібно написати програму яка покаже вміст цього
# кошика

# cookies = int(input("Введіть кількість печива: "))
#
# print("Вміст кошика:")
#
# for cookie in range(cookies):
#     print("🍪", end="")

# Завдання 2
# Бухгалтерія має згенерувати номери рахунків для
# клієнтів у форматі INV-1001, INV-1002 тощо
# Програма отримує кількість клієнтів

# customers = int(input("Введіть кількість клієнтів :"))
#
# num = 1000
#
# for i in range(customers):
#     num += 1
#     print(f"INV-{num}")
#
# print("Рахунки:")

# Завдання 3
# Ви розробляєте застосунок для планування тренувань.
# Користувач вводить раз на скільки днів він готовий
# виконувати вправи. Вам потрібно вивести всі дні протягом
# місяця(30 днів) коли треба займатись спортом.

# day = int(input("Раз на скільки днів тренуватися :"))
#
# for i in range(1, 30  ,day):
#     print(f"День тренування: {i}")

# Завдання 4
# У завданні 1 зробіть так щоб користувач сам вирішував
# що він кладе в кошик, бо не всі люблять печиво.
# З можливих варіантів 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎
# 🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 🥝

# kind = input("Введіть що ви хочете 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 🥝 :")
# more = input("Можливо що ще? (ні/так) :").upper()
#
# if more == "НІ":
#     count = int(input("Введіть кількість: "))
#
#     print("Вміст кошика:")
#
#     for cookie in range(count):
#         print(kind, end="")
# elif more == "ТАК":
#     count = int(input("Введіть кількість до першого вибору: "))
#     what = input("Що ще ви хочете? 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 🥝 :")
#     count1 = int(input("Введіть кількість до другого вибору: "))
#
#     print("Вміст кошика:")
#
#     for cookie in range(count):
#         print(kind, end="")
#     for cookie in range(count1):
#         print(what, end="")


# Завдання 5
# Напишіть програму яка виконує зворотній відлік перед
# запуском ракети.

# print("починаю зворотній відлік")
#
# for i in range(10, 0 , -1):
#     print(i)
# print("Запуск")

# Завдання 6
# Потрібно вивести на екран таблицю множення для
# певного числа. Наприклад для числа 5
# 1*5 = 5
# 2*5 =10
# …
# 10*5=50
# Виправте помилку в коді

# num = int(input("Введіть число: "))
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} * {i} = {result}")

# Завдання 7
# Перепишіть завдання 7(про вклад в банк) з теми Модуль
# 2 Змінні та типи даних. Частина 2 (файл Практична 2.2)
# використовуючи цикл


# diposit_amount = float(input("Вкажіть суму вкладу :"))
# rate = float(input("Вкажіть відсоток ставки :"))
# multiplier = 1 + rate / 100
# diposit_amount_every_year = diposit_amount * multiplier
# diposit_amount_every_year = diposit_amount_every_year * multiplier
# diposit_amount_every_year = diposit_amount_every_year * multiplier
# diposit_amount_every_year = diposit_amount_every_year * multiplier
# diposit_amount_every_year = diposit_amount_every_year * multiplier
# print(f"Сума після 5 років: {diposit_amount_every_year: .2f}")
#
# diposit_amount = float(input("Вкажіть суму вкладу :"))
# rate = float(input("Вкажіть відсоток ставки :"))
# multiplier = 1 + rate / 100
# diposit_amount_every_year = diposit_amount * multiplier
# diposit_amount_every_year2 = diposit_amount_every_year * multiplier
# diposit_amount_every_year3 = diposit_amount_every_year2 * multiplier
# diposit_amount_every_year4 = diposit_amount_every_year3 * multiplier
# diposit_amount_every_year5 = diposit_amount_every_year4 * multiplier
# print(f"Сума після 5 років: {diposit_amount_every_year: .2f}")
# print(f"Сума після 5 років: {diposit_amount_every_year2: .2f}")
# print(f"Сума після 5 років: {diposit_amount_every_year3: .2f}")
# print(f"Сума після 5 років: {diposit_amount_every_year4:.2f}")
# print(f"Сума після 5 років: {diposit_amount_every_year5: .2f}")


# diposit_amount = float(input("Вкажіть суму вкладу :"))
# rate = float(input("Вкажіть відсоток ставки :"))
#
# multiplier = 1 + rate / 100
#
# for year in range(1,6):
#     diposit_amount *= multiplier

#     print(f"Сума після {year} років: {diposit_amount: .2f}")


# Завдання 1
# Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні

# num1 = int(input("Введіть перше число :"))
# num2 = int(input("Введіть друге число :"))
#
# print("У задньому діапазоні числа:")
#
# for i in range(num1, num2 + 1):
#     print(i)

# Завдання 2
# Користувач вводить з клавіатури два числа.
# Вкажіть усі непарні числа у заданому діапазоні.

# num1 = int(input("Введіть перше число :"))
# num2 = int(input("Введіть друге число :"))
#
# print("Усі непарні числа задньому діапазоні:")
#
# for i in range(num1, num2 + 1):
#     if i % 2 != 0:
#         print(i)

# Завдання 3
# Користувач вводить з клавіатури два числа.
# Вкажіть усі парні числа у заданому діапазоні.


# num1 = int(input("Введіть перше число :"))
# num2 = int(input("Введіть друге число :"))
#
# print("Усі парні числа задньому діапазоні :")
#
# for i in range(num1, num2+ 1):
#     if i % 2 == 0:
#         print(i)

# Завдання 4
# Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні за спаданням.

# num1 = int(input("Введіть перше число :"))
# num2 = int(input("Введіть друге число :"))
#
# print("У задньому діапазоні числа за спаданням:")
#
# for i in range(num1, num2 -1):
#         print(i)

# Завдання 5
# Користувач вводить з клавіатури два числа. Вкажіть
# усі непарні числа у заданому діапазоні. Якщо межі
# діапазону вказані неправильно, потрібно провести
# нормалізацію меж. Наприклад, користувач ввів 33 і 13.
# Потрібна нормалізація, після якої початок діапазону
# дорівнюватиме 13, а кінець дорівнюватиме 33.

# num1 = int(input("Введіть перше число :"))
# num2 = int(input("Введіть друге число :"))
#
# if num1 > num2:
#     num1, num2 = num2, num1
#
# print("Непарні числа у задньому діапазоні::")
#
# for i in range(num1, num2 + 1):
#     if i % 2 != 0:
#         print(i)























