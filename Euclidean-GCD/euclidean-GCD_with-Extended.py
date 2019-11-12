from random import randint


def simple_GCD(a=int, b=int):
    while (a % b != 0):
        a, b= b, a % b
    return b


def extended_GCD(a=int, b=int):
    x = 1
    y = 0
    g = a
    r = 0
    s = 1
    t = b

    while (t > 0):
        q = g//t
        u = x - q*r
        v = y - q*s
        w = g - q*t
        x = r
        y = s
        g = t
        r = u
        s = v
        t = w
    return (g, x, y)


if __name__ == "__main__":
    print(simple_GCD(3, 2))
    print(extended_GCD(3, 2))

    print(simple_GCD(5, 2))
    print(extended_GCD(5, 2))

    print(simple_GCD(15, 3))
    print(extended_GCD(15, 3))
