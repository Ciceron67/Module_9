def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res <= 1:
            print("Составное")
            return res
        if res <= 3:
            print("Простое")
            return res
        if res % 2 == 0 or res % 3 == 0:
            print("Составное")
            return res
        if res % res == 0:
            print("Простое")
            return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
