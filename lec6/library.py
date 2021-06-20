
objects = []
g = 10


def foo(x):
    print('foo ', x, " * ", x, " = ", x*x)


def bar(a, b):
    '''Эта функция склажывает и возвращает сумму'''
    return a + b


def create_object(name):
    objects.append("object[" + name + "]")


def print_objects():
    print("Все добавленные объекьы:")
    for obj in objects:
        print(obj)


if __name__ == "__main__":
    print("Library executed separately. Let's test itself.")
    if bar(2, 2) == 4:
        print("OK")
    else:
        print("Fail")
