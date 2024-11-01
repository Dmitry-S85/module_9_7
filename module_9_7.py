def sum_three(a, b, c):
    return a + b + c

def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            if all(result % i for i in range(2, result)):
                print("Простое")
            else:
                print("Составное")
        else:
            print("Составное")

@is_prime
def sum_three_with_check(a, b, c):
    result = sum_three(a, b, c) 
    return result

result = sum_three_with_check(2, 3, 6)
print(result)