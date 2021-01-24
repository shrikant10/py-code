"""
Implement cache using decorator for a function to check a number is prime.
"""

cache = {}

def cached(func):
    def wrapper(a):
        if a not in cache:
            cache[a] = func(a)
        return cache[a]
    return wrapper


@cached
def is_prime(n):
    print('Running is prime function for ', n)

    if n <= 1: return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False

    return True

print(is_prime(48))
print(is_prime(53))
print(is_prime(48))
print(is_prime(53))
print(is_prime(48))

# Notice the output that it will not rerun is_prime again for same values instead return form cache.