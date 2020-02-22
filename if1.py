x = int(input("Возраст:"))
def lines(a):
    if a < 7:
        return ("Сад")
    if a <= 17:
        return ("Школа")
    if a <= 22:
        return ("ВУЗ")
    return ("Работает")
print(lines(x))