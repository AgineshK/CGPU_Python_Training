a, b = 0, 1
for _ in range(int(input("Enter the number:"))):
    print(a, end=",")
    a, b = b, a + b