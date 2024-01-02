"""
Используя функцию rand5(), которая возвращает целое число от 1 до 5 (включительно) 
с равномерной вероятностью, реализуйте функцию rand7(), 
которая возвращает целое число от 1 до 7 (включительно).
"""

from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    return (max(rand5() - 1, 0) + max(rand5() - 1, 0)) % 7 + 1


def main():
    a = {i: 0 for i in range(1, 8)}
    for _ in range(1000):
        a[rand7()] += 1

    print(a)


if __name__ == "__main__":
    main()
