def factor(a):
    b = 1
    print("the factors of {a}")
    while b<=a :
        if a%b == 0:
            print(b)
        b += 1
    return
factor(int(input("Enter a number for factoring: ")))
