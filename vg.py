try:
    a = input("Введите число:")
    b = input("Введите ещё одно число:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Ошибка ввода.")
    
