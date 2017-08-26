__author__ = 'FRODT'


def fib(k):
    # """
    # :param k:
    # :rtype : int
    # """
    a, b = 0, 1
    while a < k:
        print(a, end=' ')
        a, b = b, a + b
        print()
fib(200)
