from django.http import JsonResponse
import concurrent.futures


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(request, end):
    start = 1
    end = int(end)
    prime_count = sum(1 for x in range(start, end + 1) if is_prime(x))
    return JsonResponse({"prime_count": prime_count})


def calculate_primes_concurrent(request, end):
    start = 1
    end = int(end)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        prime_count = sum(executor.map(is_prime, range(start, end + 1)))
    return JsonResponse({"prime_count": prime_count})


def calculate_primes_parallel(request, end):
    start = 1
    end = int(end)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        prime_count = sum(executor.map(is_prime, range(start, end + 1)))
    return JsonResponse({"prime_count": prime_count})
