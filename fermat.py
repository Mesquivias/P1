import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    # First check to see if y = 0.
    if y == 0:
        return 1

    # Check if y is even or not.
    # Then initialize variable z from Figure 1.4
    # The book version was not recognizing my inputs as integers
    # So I struggled a bit on this part
    if (y % 2) == 0:
        z = mod_exp(x, (y / 2), N)
        return (z * z) % N
    else:
        z = x % N
        z = (z * mod_exp(x, y - 1, N) % N) % N
        return (z + N) % N


def fprobability(k):
    # The book says that the probability to return yes when N is not prime = (1/2^k)
    # That is the probability of error
    # The probability of being correct when N is prime = 1
    # The probability for being incorrect is = (1/2^k)
    # So we subtract them to get correctness.
    correct = 1
    return correct - (1 / (2 ** k))


def mprobability(k):
    # This one is similar to fprobability, except we use the value (1/4^k)
    # We follow as similar procedure as in fprobability.
    correct = 1
    return correct - (1 / (4 ** k))


def fermat(N, k):
    # According to Figure 1.8, there are k tests that must be performed
    for i in range(k):
        num = random.randint(1, (N - 1))  # Getting a random number to test

        if mod_exp(num, N - 1, N) != 1:  # Using mod_exp to check for primality
            return 'composite'
        else:
            return 'prime'


def miller_rabin(N, k):
    # You will need to implement
    # Checking for even numbers and the prime number 2 (which is even)
    if N == 2:
        return 'prime'
    if N % 2 == 0 or N == 1:
        return 'composite'

    exp = N - 1
    steps = 0

    while exp % 2 == 0:
        steps += 1
        exp //= 2

    for i in range(k):
        a = random.randint(2, N - 1)
        num = mod_exp(a, exp, N)

        if num == 1 or num == N - 1:
            continue

        for i in range(steps - 1):
            num = mod_exp(num, 2, N)
            if num == N - 1:
                break
        else:
            return 'composite'

    return 'prime'

