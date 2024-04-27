def massiv(start, end):
    mas = []
    for i in range(start, end+1):
        if i % 2 != 0:
            mas.append(i)
    return mas

start = int(input("Начало: "))
end = int(input("Конец: "))
result = massiv(start, end)
print(result)