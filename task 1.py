def count_computers(num):
    digits = list(map(int, str(num)))
    d = digits[-1]
    if d == 1:
        print(f"{num} компьютер")
    elif d in (2, 3, 4):
        print(f"{num} компьютера")
    else:
        print(f"{num} компьютеров")

num = int(input('введите число: '))
count_computers(num)