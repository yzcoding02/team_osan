import turtle as t
t.speed(0)
def second():
    t.forward(100)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(6)
    t.ontimer(second,1000)
    t.clear()
t.hideturtle()
t.left(90)
t.ontimer(second,1000)
t.mainloop()