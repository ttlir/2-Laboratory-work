Задание 1
for i in range(1, 21):
    print(i)

Задание 2
numbers = list(range(1, 11))
for num in numbers:
    print(num ** 2)

Задание 3
bread = ['white bread', 'whole wheat bread', 'rye bread']
meat = ['turkey', 'ham', 'roast beef']
vegetables = ['lettuce', 'tomato', 'onion']
sauces = ['mayonnaise', 'mustard', 'ketchup']

for b in bread:
    for m in meat:
        for v in vegetables:
            for s in sauces:
                print(b + ', ' + m + ', ' + v + ', ' + s)

Задание 4
sum_even = 0
sum_odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Сумма четных чисел от 1 до 100:", sum_even)
print("Сумма нечетных чисел от 1 до 100:", sum_odd)

Задание 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введите число для вычисления факториала: "))
result = factorial(number)
print("Факториал числа", number, ":", result)

Задание 6
# Предоставленный список персональных данных
personal_data = [
    {'name': 'Анна', 'возраст': 25, 'пол': 'ж', 'рост': 165, 'вес': 60},
    {'name': 'Петр', 'возраст': 35, 'пол': 'м', 'рост': 180, 'вес': 75},
    {'name': 'Мария', 'возраст': 30, 'пол': 'ж', 'рост': 170, 'вес': 65}
]

# Вычисление среднего возраста всех персон
total_age = 0
for person in personal_data:
    total_age += person['возраст']

average_age = total_age / len(personal_data)
print("Средний возраст всех персон:", average_age)

Задание 7
numbers = list(range(1, 11))
part_of_list = numbers[2:7]
print(part_of_list)

Задание 8
fruits = ['апельсин', 'банан', 'яблоко', 'киви']

if 'яблоко' in fruits:
    print("Список содержит яблоко.")
else:
    print("Список не содержит яблоко.")

Задание 9
my_tuple = (42, "hello", [1, 2, 3])

# Вывод кортежа целиком
print("Кортеж целиком:", my_tuple)

# Вывод отдельных элементов кортежа
print("Первый элемент:", my_tuple[0])
print("Второй элемент:", my_tuple[1])
print("Третий элемент:", my_tuple[2])

Задание 10
numbers = [1, 2, 3, 4, 5]

# Добавление числа 6 в список
numbers.append(6)

# Удаление числа 3 из списка
if 3 in numbers:
    numbers.remove(3)

# Сортировка списка в обратном порядке
numbers.reverse()

print(numbers)