# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

# nums =  [1, 8, -5, 9]
#
# print(nums)
#
# for i in range(len(nums)):
#     nums[i] *= 3
#
# print(nums)
#
# for i in range(len(nums)):
#     if nums[i] > 10:
#         nums[i] = 0
#
# print(nums)

# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

# nums = []
#
# while True:
#     num = int(input("ВВедіть число :"))
#
#     if num == -1:
#         break
#
#     nums.append(num)
#
# print("Кількість чисел:", len(nums))
# print("Сума чисел", sum(nums))
# print("Мінімальне число", min(nums))
# print("Максимальне число", max(nums))
#
# average = sum(nums) / len(nums)
#
# print("Середнє число", average)

# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

# positive = []
# negative = []
#
#
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     if number == 0:
#         break
#
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

# Завдання 4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати

# salaries = []
#
# while True:
#     salary = int(input("ВВедіть заплату :"))
#
#     if salary == -1:
#         break
#
#     salaries.append(salary)
#
# percent = int(input("Введіть відсоток на який треба збільшити усім зарплату :"))
#
# for i in range(len(salaries)):
#     salaries[i] += salaries[i] * percent / 100
#
# print("Нові зарплати:", salaries)


# Завдання 5
# Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.
# Виправіть помилку в коді

# days = int(input("Введіть кількість днів: "))
#
# temperatures = []
#
# for i in range(days):
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(1,days):
#     difference = temperatures[i] - temperatures[i - 1]
#
#     print(f"Різниця температур за {i + 1}-й день: {difference}")

# Завдання 6
# Створіть застосунок банк. Є список з рахунками
# клієнтів.
# Користувач вибирає одну з команд
# ● Додати клієнта
# ● Видалити клієнта
# ● Поповнити рахунок
# ● Зняти кошти
# ● Вихід
# При додаванні клієнта, добавте рахунок в 0грн в
# кінець списку.
# В інших випадках запросіть ID(індекс) клієнта і якщо
# він вірний, то проведіть операцію

accounts = []

while True:
    print("\n----БАНК----")
    print("1.Додати клієнта")
    print("2.Видалити клієнта")
    print("3.Поповнити рахунок")
    print("4.Зняти кошти")
    print("5.Вийти")

    command = input("Виберіть команду :")

    if command == "1":
        accounts.append(0)
        print("Клієнта додано")
        print("id нового клієнта:", len(accounts) - 1)

    elif command == "2":
        client_id = int(input("Введіть id клієнта: "))

        if 0 <= client_id < len(accounts):
            accounts.pop(client_id)
            print("Клієнта видалено")
        else:
            print("Такого клієнта не існує")

    elif command == "3":
        client_id = int(input("Введіть id клієнта: "))

        if 0 <= client_id < len(accounts):
            amount = float(input("Сума поповнення: "))

            if amount > 0:
                accounts[client_id] += amount
                print("Рахунок поповнено")
                print("Баланс", accounts[client_id])
            else:
                print("Сума повинна бути більшею за нуль")

        else:
            print("Такого клієнта не існує")

    elif command == "4":
        client_id = int(input("Введіть id клієнта: "))

        if 0 <= client_id < len(accounts):
            amount = float(input("Сума зняття: "))

            if 0 < amount <= accounts[client_id]:
                accounts[client_id] -= amount
                print("Кошти знято")
                print("Баланс:", accounts[client_id])
            else:
                print("Недостатньо коштів або неправильна сума")

        else:
            print("Такого клієнта не існує")

    elif command == "5":
        print("Дякуємо за використання банку")
        break

    else:
        print("Невідома команда")

    print("Усі рахунки:", accounts)
