print("sceglie 3 numeri: ")

a = input("numero 1: ");
b = input("numero 2: ");
c = input("numero 3: ");

a = int(a)
b = int(b)
c = int(c)

if a>b:
    if b>c:
        print(a, b, c)
    else:
        print(a, c, b)
    print(c, b, a)
else:
        print(c, a, b)


