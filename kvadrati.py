a = int(input("Введите А: "))
b = int(input("Введите В: "))

s = 0

for i in range(a, b+1):
    s += i**2

print(s)