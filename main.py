def is_happy_number(number):
    if len(str(number)) != 6:
        return False


    first_half = number // 1000
    second_half = number % 1000
    sum_first_half = sum(int(digit) for digit in str(first_half))
    sum_second_half = sum(int(digit) for digit in str(second_half))
    return sum_first_half == sum_second_half

result = is_happy_number(123420)
print("Число 123420 є щасливим:", result)





