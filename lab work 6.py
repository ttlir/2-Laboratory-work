Задание 1
def caesar_cipher(text, shift):
    """
    Функция для шифрования текста методом шифра Цезаря.

    Параметры:
    - text: строка для шифрования.
    - shift: целое число - величина сдвига для шифрования.

    Результат:
    - Возвращает зашифрованный текст.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Определяем тип символа (верхний регистр или нижний)
            if char.isupper():
                alphabet_start = ord('A')
            else:
                alphabet_start = ord('a')
            
            # Применяем сдвиг с учетом границ алфавита (26 букв)
            shifted_char = chr((ord(char) - alphabet_start + shift) % 26 + alphabet_start)
            encrypted_text += shifted_char
        else:
            # Если символ не буква, оставляем его без изменений
            encrypted_text += char
    return encrypted_text

# Пример использования функции
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)

Задание 2
global_variable = "глобальная"

def demonstrate_variables():
    local_variable = "локальная"
    print("Внутри функции:")
    print("Локальная переменная:", local_variable)
    print("Глобальная переменная:", global_variable)

# Пример использования функции
demonstrate_variables()

# Попытка доступа к локальной переменной извне функции приведет к ошибке
# print("Локальная переменная:", local_variable)

# Изменение глобальной переменной изнутри функции
global_variable = "новая глобальная"
print("\nПосле изменения глобальной переменной:")
print("Глобальная переменная:", global_variable)

Задание 3
def example_function(required_param, default_param="default_value"):
    print("Обязательный параметр:", required_param)
    print("Параметр по умолчанию:", default_param)
    print()

# Вызов функции с обоими аргументами
print("Вызов функции с обоими аргументами:")
example_function("значение_1", "значение_2")

# Вызов функции только с обязательным аргументом
print("Вызов функции только с обязательным аргументом:")
example_function("значение_1")

# Вызов функции с изменением параметра по умолчанию
print("Вызов функции с изменением параметра по умолчанию:")
example_function("значение_1", "новое_значение_2")

Задание 4
def calculate_statistics(numbers):
    """
    Функция для вычисления минимального, максимального и среднего значений из списка чисел.

    Параметры:
    - numbers: список чисел.

    Результат:
    - Возвращает кортеж из трех значений: минимальное, максимальное и среднее.
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

# Пример использования функции
numbers_list = [5, 10, 15, 20, 25]
minimum, maximum, average = calculate_statistics(numbers_list)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Среднее значение:", average)

Задание 5
# Форматирование с указанием индексов
name = "Alice"
age = 30
formatted_string = "Привет, {0}! Тебе {1} лет.".format(name, age)
print(formatted_string)

# Форматирование без указания индексов
quantity = 3
item = "яблока"
formatted_string = "У вас есть {} {}.".format(quantity, item)
print(formatted_string)

# Форматирование с ключевыми словами
price = 2.50
product = "молоко"
formatted_string = "Цена за {product}: {price:.2f} руб.".format(product=product, price=price)
print(formatted_string)