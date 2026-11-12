# Завдання 1
# Користувач вводить радіус кола. Потрібно обрахувати
# площу круга та вивести результат з двома знаками після
# коми.
# Розтавте команди нижче у правильному порядку та
# додайте підписи з описом що робить команда(є
#продовження на наступній сторінці)

# radius = float(input("Введіть радіус: "))
# pi = 3.1415
# area = pi * radius ** 2
# print(f"Площа кола: {area:.2f}")

# Завдання 2
# Користувач вводить ціну однієї кружки та загальний
# бюджет. Виведіть скільки кружок можна купити
# Приклад

# price_cup = float(input("Ціна однієї кружки :"))
# budget = float(input("Введіть бюджет :"))
# result_cup = budget // price_cup
# print(f"Можна купити: {result_cup: .0f} кружок")

# Завдання 3
# Користувач вводить довжину в метрах. Виведіть цю
# довжину в футах та ярдах.
# 1 метр = 3.2808399 фута
# 1 метр = 1.0936133 ярда

# length = float(input("Введіть довжину в метрах :"))
# futs = length * 3.2808399
# yards = length * 1.0936133
#
# print(f"Довжина в футах: {futs: .2f}")
# print(f"Довжина в ярдах: {yards: .2f}")

# Завдання 4
# У завданні 2 виведіть ще залишок коштів

# price_cup = float(input("Ціна однієї кружки :"))
# budget = float(input("Введіть бюджет :"))
# result_cup = budget // price_cup
# remainder = budget % price_cup
# print(f"Можна купити: {result_cup: .0f} кружок")
# print(f"Залишок: {remainder: .2f}")

# Завдання 5
# Користувач вводить загальну кількість хвилин.
# Переведіть їх у години та хвилини.

# total_minutes = float(input("Введіть загальну кількість хвилин :"))
# hours = total_minutes / 60
# seconds = total_minutes * 60
#
# print(f"Годин: {hours: .1f}")
# print(f"Секунд: {seconds: .0f}")

# Завдання 6
# Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока.
# Користувач вводить кількість яблук та молока(у літрах).
# Виведіть скільки він може спекти пирогів.
# Виведіть скільки яблук та молока залишиться.

# apples = float(input("Кількість яблук :"))
# milk = float(input("Кіліькість молока у (л) :"))
# pies_apples = apples // 4
# pies_milk = milk // 1.2
#
# pies = min(pies_apples, pies_milk)
# apples_left = apples - pies * 4
# milk_left = milk - pies * 1.2
# print(f"Можна спекти пирогів: {pies: .0f}")
# print(f"Залишиться яблук: {apples_left: .0f}")
# print(f"Залишиться молока: {milk_left: .0f}")


# Завдання 7
# Користувач вводить суму вкладу в банк та відсоток
# ставки.
#  Обчисліть скільки користувач отримує через 5 років,
# якщо кожного року сума вкладу збільшується на даний
# відсоток
# Виведіть суму вкладу кожного року окремо


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

# Завдання 8
# Користувач вводить кількість днів. Виведіть скільки це
# років, тижнів та днів.

days = float(input("Введіть кількість днів :"))
years = days // 365
years1 = days % 365
week = years1 // 7
days1 = years1 % 7
print(f"{days: .0f} днів - це {years: .0f} рік, {week: .0f} тижнів та {days1: .0f} днів")