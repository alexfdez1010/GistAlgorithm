from typing import List, Tuple
from random import randint


def partition(array: List[int], pivot: int, left: int, right: int) -> Tuple[List[int], int]:
    pivot_value = array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    i = left
    for j in range(left, right):
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[right], array[i] = array[i], array[right]
    return array, i


def find_median(array: List[int]) -> float:
    n = len(array)
    pivot = -1
    middle = n // 2
    left = 0
    right = n - 1
    while pivot != middle:
        pivot = randint(left, right)
        array, pivot = partition(array, pivot, left, right)
        if pivot > middle:
            right = pivot - 1
        elif pivot < middle:
            left = pivot + 1

    if n & 1:
        return array[pivot]
    else:
        return (array[pivot] + max(array[:pivot])) / 2


def main():
    array = list(map(int, input().split()))
    print(find_median(array))


def test():
    for i in range(10000):
        array = [randint(1, 10000) for _ in range(randint(1, 10000))]
        n = len(array)
        sorted_array = sorted(array)
        if n & 1:
            assert find_median(array) == sorted_array[n // 2]
        else:
            assert find_median(array) == (sorted_array[n // 2] + sorted_array[n // 2 - 1]) / 2
        print(f"Test {i+1} passed")


if __name__ == '__main__':
    test()
