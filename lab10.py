from array import array
from ctypes import Array
from typing import Tuple

def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    start= 0
    end = len(numbers)-1
    middle = 0

    while numbers is not None:

        middle = (start + end) // 2

        if numbers[middle] == value:
            return True, value

        elif numbers[middle] < value:
            start += 1

        elif numbers[middle] > value:
            end -= 1

    return False, -1  # wartosc nie zostala znaleziona

ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])


result = binary_search(ints, 7)
print(result)
