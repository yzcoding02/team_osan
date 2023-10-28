import turtle as t
class CturtleConfig:
    def __init__ (self,색="black"):
        self.객체=t.Turtle()
        self.색=색
        self.settings()
    def settings(self):
        self.객체.color(self.색)
        self.객체.shape("turtle")        
        self.객체.penup()
    def comehome():
        t.home()
    
t1=CturtleConfig("red")
t.onscreenclick(t1.객체.goto,1)
t.onkey(t1.객체.home,"1")
t2=CturtleConfig("blue")
t.onscreenclick(t2.객체.goto,3)
t.onkey(t2.객체.home,"2")
t.mainloop()
t.listen()