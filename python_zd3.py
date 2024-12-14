# Задача 1: Вывод элементов, которые меньше 15
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
elements_less_than_15 = [x for x in a if x < 15]
print("Элементы, которые меньше 15:", elements_less_than_15)

# Задача 2: Определение, положительное ли число, отрицательное или равно нулю
number = float(input("Введите число: "))
if number > 0:
    print("Положительное число")
elif number < 0:
    print("Отрицательное число")
else:
    print("Число равно нулю")

# Задача 3: Простой арифметический калькулятор
def calculator():
    print("Введите два числа:")
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    operation = input("Введите номер операции (1/2/3/4): ")
    
    if operation == '1':
        result = num1 + num2
        print("Результат:", result)
    elif operation == '2':
        result = num1 - num2
        print("Результат:", result)
    elif operation == '3':
        result = num1 * num2
        print("Результат:", result)
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print("Результат:", result)
        else:
            print("Ошибка: Деление на ноль!")
    else:
        print("Неверная операция")

calculator()

# Задача 4: Программа обратного отсчета от 10 до 1
print("Обратный отсчет от 10 до 1:")
for i in range(10, 0, -1):
    print(i)

# Задача 5: Решение квадратного уравнения
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "Нет действительных корней"

# Ввод коэффициентов
print("Решение квадратного уравнения ax^2 + bx + c = 0")
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic(a, b, c)
print("Корни квадратного уравнения:", roots)