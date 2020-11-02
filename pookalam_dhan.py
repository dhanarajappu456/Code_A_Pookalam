#code a pookalam
import turtle as t
win = t.Screen()

t.speed(0)


def circ(t, rad, cl):
    t.home()
    t.rt(90)
    t.pu()
    t.fd(rad)
    t.lt(90)
    t.pd()
    t.pen(pencolor=cl, pensize='1', fillcolor=cl)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.pu()
    t.home()


t.speed(0)


def _square(t, r, cl):
    t.pen(pencolor=cl, pensize='1', fillcolor=cl)
    t.begin_fill()
    for j in range(4):
        t.fd(0.707*r)
        t.lt(90)
    t.end_fill()


def draw_lines(t, lnt, an):
    t.pu()
    t.home()
    for i in range(0, 37):
        t.pd()
        ang = i*10
        ang += an

        t.rt(ang)
        t.forward(lnt)
        t.pu()
        t.home()


def multiplecircle(t, r, n):
    t.circle(r/2)
    t.lt(60)


def _innersquare(t, r):
    for j in range(4):
        t.fd(0.707*r)
        t.lt(90)


def petal(t, r, cl):
    t.pen(pencolor=cl, pensize='1', fillcolor=cl)
    t.begin_fill()
    for i in range(2):
        y = 1.743*(r/2)
        t.circle(y, 70)
        t.left(110)
    t.end_fill()


def flower(n, t, r, cl):
    for i in range(1, n+1):
        petal(t, r, cl)
        t.lt(360/n)


circ(t, 380, "#660000")                            # brown
circ(t, 360, "#c70000")                            # variation red
t.pen(pencolor='black', pensize="7")
draw_lines(t, 358, 0)
t.pen(pencolor='black', pensize="1")
circ(t, 340, "#e5563d")                            # light red shade
t.pen(pencolor='black', pensize="7")
draw_lines(t, 338, 15)
circ(t, 320, "#f5c050")                            # yellow light
t.home()

for j in range(1, 37):
    _square(t, 320, "#f96302")                     # orange var
    t.lt(360/36) 

circ(t, 292, "#FFCC11")                            # yellow var
t.home()
flower(8, t, 292, "#FAEDEB")                       # light red
t.home()
t.lt(15)
flower(8, t, 292, "#EBB8AF")                       # zinwalidate
t.lt(15)
flower(8, t, 292, "#CD4F39")                       # tomato 3
t.home()
circ(t, 210, "#414F12")
circ(t, 200, "#C6CF85")

for i in range(6):
    t.pd()
    t.begin_fill()
    if(i % 2 == 0):
        t.pen(pencolor="#000000", fillcolor="#000000", pensize="1")
        multiplecircle(t, 200, 24)
    else:
        t.pen(pencolor="#FF0000", fillcolor="#FF0000", pensize="1")
        multiplecircle(t, 200, 24)
    t.end_fill()

circ(t, 143, "black")
circ(t, 140, "#D4AF37")                            # yellow variant
t.home()
flower(8, t, 140, "#008B8B")                       # dark cyan
t.home()
t.lt(15)
flower(8, t, 140, "#C0C0C0")                       # silver
t.lt(15)
flower(8, t, 140, "#CD4F39")                       # red shade
t.home()
circ(t, 90, "#E6E6FA")                             # lavendar
t.lt(45)
t.pd()

for i in range(6):
    t.begin_fill()
    _innersquare(t, 90)
    if(i % 2 == 0):
        t.pen(pencolor="yellow", fillcolor="yellow")
    else:
        t.pen(pencolor="orange", fillcolor="orange")
    t.end_fill()
    t.lt(60)

t.home()
t.pd()
t.color("green")
t.dot(20)
t.getscreen().getcanvas().postscript(file='out.ps')
t.mainloop()
