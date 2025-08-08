import math
def prime_preprocessing(n):
    is_prime_list = [True] * (n+1)
    is_prime_list[0] = is_prime_list[1] = False

    for i in range(2,math.ceil(n**0.5)):
        if is_prime_list[i]:
            for j in range(i*i,n+1,+i):
                is_prime_list[j] = False

    for i in range(2,n+1):
        if is_prime_list[i]:
            print(i)

prime_preprocessing(int(input("Enter the total number of primes you want : ")))