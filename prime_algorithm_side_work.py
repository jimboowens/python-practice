# prime numbers are only divisble by 1 and itself

user_num = int(raw_input("What number do you want to test? "))
prime_factors = []
user_product = 1

for i in range (2,user_num / 2 + 1):
        if (user_num % i == 0):
                prime_factors.append(i)
                user_product = user_product * i 
                if (user_product == user_num):
                         break
print prime_factors