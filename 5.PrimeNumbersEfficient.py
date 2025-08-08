from math import sqrt

def prime_preprocessing(n):
    count = 0
    true_primes = {}
    for i in range(2,n+1):
        true_primes[i] = True
    for i in true_primes.keys():
        if true_primes[i]:
            j = i*i
            while j in true_primes.keys():
                if true_primes[j] is True:
                    true_primes[j] = False
                j+=i
            count+=1
            print(i)

prime_preprocessing(int(input("Enter the total number of primes you want : ")))