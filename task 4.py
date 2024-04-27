def ymnozenie(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f"{i * j}", end=" ")
        print()

num = int(input("Введите число: "))
ymnozenie(num)