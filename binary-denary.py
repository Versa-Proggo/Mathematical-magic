def binary_to_denary(binary_str):
    denary=0
    power=0
    for digit in reversed(binary_str):
        if digit not in("0","1"):
            print("Invalid binary number!")
            return
        denary+=int(digit)*(2**power)
        power+=1
    print(f"Binary {binary_str} = Denary {denary}")
binary=input("Enter a binary number: ")
binary_to_denary(binary)
