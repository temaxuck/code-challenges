"""
Problem:
    Мы можем определить, насколько массив A «не по порядку», 
    подсчитав количество инверсий, которые он имеет. 
    Два элемента A[i] и A[j] образуют инверсию, если A[i] > A[j], но i < j. 
    То есть меньший элемент появляется после большего элемента.

    Дан массив. Подсчитайте количество инверсий, которые он имеет. 
    Сделайте это быстрее, чем время O(N^2).

    Вы можете предположить, что каждый элемент массива уникален.

    Например, отсортированный список не имеет инверсий. 
    Массив [2, 4, 1, 3, 5] имеет три инверсии: (2, 1), (4, 1) и (4, 3). 
    Массив [5, 4, 3, 2, 1] имеет десять инверсий: каждая отдельная пара образует инверсию.
    
Notes:
    Solved with the help of AI (the idea to use merge sort, a way to count inversions)
    and Internet (merge sort implementation)
    
    My ideas to solve this problem were:
        - Use dict which keys would be values of `a` and values how many numbers in `a`
          are larger than the key value. Then to do something with indexes of the key value.
        - I don't remember another
"""
from random import randint
from collections import OrderedDict


def solution(a, inversions=0):
    l_inversions = 0
    r_inversions = 0
    if len(a) > 1:
        mid = len(a) // 2

        l = a[:mid]
        r = a[mid:]

        _, l_inversions = solution(l, inversions)
        _, r_inversions = solution(r, inversions)

        li, ri, ai = 0, 0, 0  # left, right, source lists' indexes

        while li < len(l) and ri < len(r):
            if l[li] <= r[ri]:
                a[ai] = l[li]
                li += 1
            else:
                inversions += len(l) - li
                a[ai] = r[ri]
                ri += 1
            ai += 1

        while li < len(l):
            a[ai] = l[li]
            ai += 1
            li += 1

        while ri < len(r):
            a[ai] = r[ri]
            ai += 1
            ri += 1

    return a, l_inversions + r_inversions + inversions


def main():
    # generate a random list of random size of unique values
    a = list(
        OrderedDict.fromkeys([randint(0, 15) for _ in range(randint(5, 10))]).keys()
    )
    print(a)
    print(solution(a)[1])


if __name__ == "__main__":
    main()
