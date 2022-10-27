#zadanie 1
def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    numbers(n - 1)

numbers(10)

#zadanie 2
def fib(n: int) -> int:
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print("Zadanie 2:")
print(fib(6))

#zadanie 3
def power(number: int, n: int) -> int:
    if n == 0:
        return 1

    return (number * power(number, n - 1))

print("Zadanie 3:")
print(power(2,3))

#zadanie 4
def reverse(txt: str) -> str:
    str = ""
    for i in txt:
        str = i + str
    return str

print("Zadanie 4:")
print(reverse('michal'))

#zadnie 5
def factorial(n: int) -> int:
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n - 1))

print("Zadanie 5:")
print(factorial(4))

#zadanie 6
def prime(n: int) -> bool:
    for i in range(2, 1 + n // 2):
        if n % i == 0:
            return False
    return True

print('Zadanie 6:')
print(prime(6))
print(prime(7))

#zadanie 7
