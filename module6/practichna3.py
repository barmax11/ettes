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
