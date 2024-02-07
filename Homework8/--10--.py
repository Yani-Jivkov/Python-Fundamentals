def check_perfect_number():
    num = int(input())

    sum_of_divisors = 1

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i

    if sum_of_divisors == num and num != 1:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

check_perfect_number()
