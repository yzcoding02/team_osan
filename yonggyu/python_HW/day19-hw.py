import turtle as t
t.speed(0)
def allClear(x,y):
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

t.onkey(scircle,"s")
t.onkey(mcircle,"m")
t.onkey(bcircle,"b")
t.onscreenclick(jump)
t.onscreenclick(allClear,3)
'''3 is rmb '''

t.listen()
t.mainloop()