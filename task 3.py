def massiv(start, end):
    mas = []
    for i in range(start, end+1):
        if i % 2 != 0:
            mas.append(i)
    return mas

start = int(input("начало"))
end = int(input("конец"))
result = massiv(start, end)
print(result)