# Завдання 1
# Користувач вводить суму на рахунку в банку та суму
# покупки. Виведіть на екран залишок коштів.
# suma_rahunok = int(input("Введіть суму рахунку: "))
# suma_pokupku = int(input("Введіть суму покупки: "))
#
# num3 = int(num1 - num2)
# print("Залишок становить:", num3)

# Завдання 2
# Напишіть програму яка запитує в користувача ціну
# однієї чашки кави(може бути з копійками) та кількість
# чашок.
# nmu1 = float(input("Яка ціна однієї чашки кави? :"))
# nmu2 = int(input("Скільки чашок потрібно? :"))
#
# nmu3 = float(nmu1 * nmu2)
# print("Сума замовлення становить:", nmu3)

# Завдання 3
# Потрібно порахувати площу прямокутника. Але
# програма видає помилку

# width = float(input("Введіть ширину: "))
# height = float(input("Введіть висоту: "))
# area = width * height
# print("Площа дорівнює:", area)


#результат чат бота
# width = float(input("Введіть ширину: "))
# height = float(input("Введіть висоту: "))
#
# area = width * height
#
# print("Площа дорівнює:", area)

# Завдання 4
# Ви обідаєте з друзями в ресторані і вирішуєте скільки
# залишити чайових.
# Користувач вводить суму рахунку та відсоток
# чайових(наприклад 10, 15 чи 20).
# Виведіть чайові та загальну суму на окремих рядках з
# підписами

# suma_rahunku = float(input("Введіть суму рахунку :"))
# tips = float(input("Введіть відсоток чайових :"))
#
# tips1 = float(suma_rahunku * tips / 100)
# all_suma_rahunku = float(suma_rahunku + tips1)
#
# print("Ось ваші чайові:", tips1)
# print("Ось ваша сума рахунку:", all_suma_rahunku)

# Завдання 5
# Потрібно спланувати витрати на поїздку.
# Користувач вводить
# відстань в км
# витрати пального на 100 км в літрах
# ціна 1 л пального
# Виведіть на екран кількість пального та його ціну

# distance = float(input("\tВведіть відстань в кілометрах: "))
# loss_fuel = float(input("\tВведіть витрату пального на 100 км в літрах: "))
# price_1liter = float(input("\tВведіть ціну одного літру пального: "))
#
# fuel_used = float(distance * loss_fuel / 100)
# trip_cost = float(fuel_used * price_1liter)
#
# print("Ось скільки пального використається:", fuel_used)
# print("Ось яка буде вартість пального:", trip_cost)

# Завдання 6
# Користувач вводить два числа, програма повинна
# вивести суму, різницю та добуток. Але програма не працює
# num1 = int(input("перше число: "))
# num2 = int(input("друге число: "))
# result = num1 + num2
# result = num1 - num2
# result = num1 * num2
# print(result)



# num1 = int(input("перше число: "))
# num2 = int(input("друге число: "))
# result1 = num1 + num2
# result2 = num1 - num2
# result3 = num1 * num2
# print("Сума чисел:", result1)
# print("Різниця чисел:",result2)
# print("Добуток чисел:",result3)


#рішення хелпера
# num1 = int(input("Перше число: "))
# num2 = int(input("Друге число: "))
#
# sum_result = num1 + num2
# difference = num1 - num2
# product = num1 * num2
#
# print("Сума:", sum_result)
# print("Різниця:", difference)
# print("Добуток:", product)

# Завдання 7
# Ви вирішили покинути ресторан.
# У завданні 4 модифікуйте код так, щоб ще вводилась
# кількість людей і виводило на екран скільки має заплатити
# кожен(включно з чайовими)

# suma_rahunku = float(input("Введіть суму рахунку :"))
# tips = float(input("Введіть відсоток чайових :"))
# all_customers = int(input("Введіть кількість людей: "))
#
# tips1 = float(suma_rahunku * tips / 100)
# all_suma_rahunku = float(suma_rahunku + tips1)
# per_person = all_suma_rahunku / all_customers
#
# print("Ось ваші чайові:", tips1)
# print("Ось ваша сума рахунку:", all_suma_rahunku)
# print("Кожен платить:", per_person)


# Завдання 8
# Менеджер магазину просить вас перевірити скрипт для
# підрахунку здачі покупцеві. Виправте помилку в коді

# a = float(input("Введіть суму грошей покупця: "))
# b = float(input("Введіть вартість товару: "))
# if a >= b:
#     c = a - b
#     print("Здача:", c)
# if a <b:
#     print("Недостатньо грошів")

# Завдання 9
# Напишіть програму, яка запитує у користувача:
# 1. ім’я
# 2. рік народження
# 3. зріст у метрах

name = input("Введіть ваше ім'я :")
year_born = int(input("Введіть ваш рік народження :"))
height = float(input("Введіть ваш ріст у метрах :"))
year = 2026
year_born1 = (year - year_born)
print("---АНКЕТА КОРИСТУВАЧА---")
print("\tІм'я:", name)
print("\tВік:", year_born1, "років")
print("\tЗріст:", height, "м")





