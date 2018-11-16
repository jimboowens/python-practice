# prime numbers are only divisble by 1 and itself

user_num = int(raw_input("What number do you want to test? "))
user_num_indexed = user_num
prime_factors = []

for i in range (2,user_num_indexed / 2 + 1):
        if (user_num_indexed % i == 0):
                prime_factors.append(i)
                user_num_indexed = (user_num_indexed / i)
                for i in range (0, len(prime_factors)):
                        if (int(prime_factors(i)) == user_num_indexed):
                                break
                print "%i is i" %i
                i = 2
                print "%i is user num indexed" %user_num_indexed
                print "%s is primes" %str(prime_factors)
        else:
                print "%i is not a divisor" %i
# poop

print prime_factors