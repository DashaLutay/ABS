def task_1(a:int = 1, b:float = 1.15, c:str = 'пончик', d:list = [1, 2, 3], e:bool = True) -> tuple:
    return type(a), type(b), type(c), type(d), type(e)
print(task_1())


def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]

print(task_2())


def task_3(a) -> int:
    return a**2

a = task_3(4)
print(a)
