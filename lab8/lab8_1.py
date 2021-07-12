import turtle
turtle.speed('fastest')


def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)

#draw(400, 3)

# https://mipt-cs.github.io/python3-2017-2018/labs/lab8.html


def draw2(l, n):
    if n == 0:
        turtle.forward(l / 3)
        turtle.left(60)
        turtle.forward(l / 3)
        turtle.right(120)
        turtle.forward(l / 3)
        turtle.left(60)
        turtle.forward(l / 3)
        return
    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x / 3)
        turtle.left(60)

        draw2(x, n - 1)
        turtle.forward(x / 3)
        turtle.right(120)
        turtle.forward(x / 3)
        turtle.left(60)
        turtle.forward(x / 3)


draw2(400, 2)
input()
