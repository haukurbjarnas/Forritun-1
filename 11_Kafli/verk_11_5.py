def prime_sum(n):
    factor_constant = 2
    sum_of_primes = 0
    factors_list = []
    loop_list = n[:].split(",")
    loop_check = 0

    for i in loop_list:
        for i in range(2,100):
            if int(i) % factor_constant == 0:
                loop_check += 1
            factor_constant += 1
        if factor_constant == 0:
            factors_list.append(i)        
    
    for i in factors_list:
        sum_of_primes += i

    return sum_of_primes


runa = input("")

ksi_paul = prime_sum(runa)

print(ksi_paul)