def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Неизвестная операция"


print("Простой калькулятор")
print(calculate(10, "+", 5))
print(calculate(10, "/", 0))