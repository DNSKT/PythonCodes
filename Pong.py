#snake game

import turtle
import os
import random


wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)

#movement
def go_up():
    y = head.ycor()
    head.sety(y+20)
def go_down():
    y = head.ycor()
    head.sety(y-20)
def go_left():
    x = head.xcor()
    head.setx(x-20)
def go_right():
    x = head.xcor()
    head.setx(x+20)

#score
score = 0

#high score
high_score = 0


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#displays score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        head.goto(0,0)
        head.direction = "stop"

    #check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        #add to the score
        score += 10
        #update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        #check if the score is higher than the high score
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #reset the score to 0 if the score is less than 0
        if score < 0:
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))