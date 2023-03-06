a: int = 5
b: str = 'строка'
с: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))


def asd(s: str = "") -> int:
    return len(s)

print (asd())


def zxc(x:list, y: list) -> int:
    return max (len(x), len(y))

print(zxc([1,2], [1, 2, 3, 4]))
