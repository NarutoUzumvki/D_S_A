def check_armstrong(num):
    length = len(str(num))
    # print(length)
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp = temp // 10
    if num == sum :
        print(f"{num} is an armstrong Number.")
    else:
        print(f"{num} is not an Armstrong Number.")

check_armstrong(1634)