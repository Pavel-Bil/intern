def massiv(start, end):
    mas = []
    for num in range(start,end + 1):
        if num > 1:
            for i in range(2, num // 2 + 1):
                if (num % i) == 0:
                    break
            else:
                mas.append(num)
    return mas

start = int(input("Начало: "))
end = int(input("Конец: "))

print("Простые числа в диапазоне от", start, "до", end, ":")
print(massiv(start, end))