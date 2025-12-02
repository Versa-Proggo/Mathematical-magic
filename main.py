def armstrong_number_check(num):
    org_num = num
    sum = 0
    total_digit = len(str(num))
    while(num>0):
        last_digit = num%10
        sum += last_digit**total_digit
        num//=10
    if sum == org_num:
        print(f"{org_num} is an armstrong")
    else:
        print(f"{org_num} is not an armstrong")
num = int(input("Enter a number: "))
armstrong_number_check(num)