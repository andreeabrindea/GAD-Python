def your_function(*args, **kwargs):
    """Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
numere întregi sau reale."""

    s = 0
    if type(args) == int or type(args) == float:
        s = s + args
    return s


print(your_function(1, 5, -3, "abc", [12, 56, "cad"]))


def sum(n):
    # suma tuturor numerelor de la [0, n]
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


print(sum(5))


def sum_even(n) -> int:
    # suma numerelor pare de la [0, n]
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return n + sum_even(n - 1)
        else:
            return 0 + sum_even(n - 1)


print(sum_even(6))


def sum_odd(n) -> int:
    # suma numerelor impare de la [0, n]
    if n == 0:
        return 0
    if n % 2 == 0:
        return sum_odd(n - 1)
    else:
        return n + sum_odd(n - 1)


print(sum_odd(6))


def is_integer():
    n = input("Enter a number: ")
    try:
        print(int(n))
    except ValueError:
        print(0)


is_integer()
