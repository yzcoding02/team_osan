import turtle as t
t.speed(0)
def allClear():
    t.clear()
def jump(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def scircle():
    t.circle(40)
def mcircle():
    t.circle(80)
def bcircle():
    t.circle(120)
def red():
    t.color("red")
def blue():
    t.color("blue")
def green():
    t.color("green")
def white():
    t.color("white")
def thick():
    t.pensize(5)
def thin():
    t.pensize(1)
t.onkey(scircle,"1")
t.onkey(mcircle,"2")
t.onkey(bcircle,"3")
t.onscreenclick(jump)
t.onkey(allClear,"c")
t.onkey(red,"r")
t.onkey(blue,"b")
t.onkey(green,"g")
t.onkey(white,"w")
t.onkey(thick,"t")
t.onkey(thin,"h")
t.ondrag(t.goto)
t.listen()
t.mainloop()