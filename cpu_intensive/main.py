# main.py
from fastapi import FastAPI
import concurrent.futures

app = FastAPI()


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


@app.get("/calculate_primes/{end}")
def calculate_primes_endpoint(end):
    print(f"Got the Request")
    start = 1
    end = int(end)
    prime_count = sum(1 for x in range(start, end + 1) if is_prime(x))

    return {"prime_count": prime_count}


@app.get("/calculate_primes/concurrent/{end}")
def calculate_primes_endpoint(end):
    print(f"Got the Request")
    start = 1
    end = int(end)
    # Using ThreadPoolExecutor for concurrency
    with concurrent.futures.ThreadPoolExecutor() as executor:
        prime_count = sum(executor.map(is_prime, range(start, end + 1)))

    return {"prime_count": prime_count}

@app.get("/calculate_primes/parallel/{end}")
def calculate_primes_parallel_endpoint(end):
    print(f"Got the Request")

    start = 1
    end = int(end)

    # Using ProcessPoolExecutor for parallelism
    with concurrent.futures.ProcessPoolExecutor() as executor:
        prime_count = sum(executor.map(is_prime, range(start, end + 1)))

    return {"prime_count": prime_count}
