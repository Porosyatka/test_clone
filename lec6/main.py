import library as lib


def printer():
    print(x)


def modifier():
    global x
    x += 10
    print(x)


print('Main module', __name__)

lib.foo(3)
lib.foo(4)
x = lib.bar(4, 7)
print(x)
lib.create_object("petia")
lib.create_object("Vasia")
lib.create_object("Sveta")

lib.print_objects()
print(lib.objects)
print(lib.g)

for obj in lib.objects:
    if "petia" in obj:
        print("Naiden! petia")

lib.objects.pop()
print(lib.objects)

printer()
modifier()
printer()
