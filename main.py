import tkinter
import turtle
import math
import random


root = tkinter.Tk()

board_finished = False
speed = 500

# app functions


def myfunction(target_screen):
    print("hello world")
    target_screen.clear()

# drawing functions


def fillSquare(turtle_instance, shade):
    if shade == 0:
        return
    starting_x_point = turtle_instance.xcor()
    starting_y_point = turtle_instance.ycor()
    # fill the current square
    shade = shade
    scale_size = 25
    break_point = scale_size / shade
    angle_turn = math.degrees(math.atan(break_point/scale_size))
    travel_distance = math.sqrt((scale_size ** 2)+(break_point ** 2))

    for i in range(shade):
        print(angle_turn)
        if i % 2 == 0:
            turtle_instance.right(angle_turn)
            turtle_instance.forward(travel_distance)
            turtle_instance.setheading(180)
        else:
            turtle_instance.left(angle_turn)
            turtle_instance.forward(travel_distance)
            turtle_instance.setheading(0)
    # return to current square starting point
    turtle_instance.penup()
    turtle_instance.goto(starting_x_point, starting_y_point)
    turtle_instance.pendown()
    turtle_instance.setheading(0)


def drawSquare(turtle_instance):
    turtle_instance.setheading(0)
    turtle_instance.forward(25)
    turtle_instance.setheading(270)
    turtle_instance.forward(25)
    turtle_instance.setheading(180)
    turtle_instance.forward(25)
    turtle_instance.setheading(90)
    turtle_instance.forward(25)
    turtle_instance.setheading(0)


def drawBoard(turtle_instance, draw_square, fill_square):
    global board_finished
    if (not board_finished):
        for i in range(20):
            print(i)
            if i > 0:
                turtle_instance.setheading(270)
                turtle_instance.forward(25)
                turtle_instance.setheading(180)
                turtle_instance.forward(500)
                turtle_instance.setheading(0)
            for j in range(20):
                print(j)
                draw_square(turtle_instance)
                shader = random.random()
                fill_square(turtle_instance, math.floor(shader * 10))
                turtle_instance.forward(25)
    board_finished = True


def main(turtle_instance):
    turtle_instance.color("white")
    turtle_instance.penup()
    turtle_instance.goto(-250, 250)
    turtle_instance.pendown()


# initail objects
canvas = tkinter.Canvas(root, width=500, height=500)
canvas.grid(column=0, row=3, columnspan=2)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")

# tkinter Widgets
button = tkinter.Button(
    root, text="hello", command=lambda: print("hello world"))
button.grid(column=0, row=0)

# turtle objects
pen = turtle.RawTurtle(screen)
pen.speed(speed)


if __name__ == "__main__":
    main(pen)
    while True:
        drawBoard(pen, drawSquare, fillSquare)
        root.update_idletasks()
        root.update()
