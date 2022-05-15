from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления квадратного корня из заданного числа.'


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        print(f'Введите позитивное число')
        return False
    print(f'Мы вычислили корень квадратный из введенного вами числа. Это будет: {calculatesquareroot(your_number)}')


print(message)
calc(25.5)
