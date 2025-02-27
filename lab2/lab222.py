def get_divisors(n):
    
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  
                divisors.append(n // i)
    return divisors

def calculate_M(n):
    
    divisors = get_divisors(n)
    if not divisors:
        return 0
    return min(divisors) + max(divisors)


start_number = 452021
found_numbers = []


for number in range(start_number + 1, 1000000):  
    M = calculate_M(number)
    if M % 7 == 3:
        found_numbers.append((number, M))
        if len(found_numbers) == 5:
            break

for num, M in found_numbers:
    print(num, M)
