from turtle import *

def d_cir(x, y, f_color, red):
    goto(x,y)
    down()
    begin_fill()
    fillcolor(f_color)
    circle(red)
    end_fill()
    up()
    home()
up()
pensize(4)
d_cir(0,-50,"green",50)
d_cir(150,150,"orange",50)
d_cir(-150,150,"blue",50)
d_cir(-150,-150,"red",-50)
d_cir(150,-150,"yellow",-50)

hideturtle()
done()
done()

