def delenie(num):
    min_num = min(num)
    delitel = []
    for i in range(1, min_num + 1):
        if all(n % i == 0 for n in num):
            delitel.append(i)
    return delitel

num = [45, 15, 90]
result = delenie(num)
print(result)

