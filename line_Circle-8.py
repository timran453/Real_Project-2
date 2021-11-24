from turtle import *

list1 = ["red","green","yellow","blue"]
list2 = ["red","green","yellow","blue","orange","brown"]
up()
goto(200,-200)
for i in range(4):
    down()
    begin_fill()
    fillcolor(list1[i])
    circle(50)
    end_fill()
    up()
    bk(100)

home()
goto(200,50)

for i in range(6):
    down()
    color(list2[i])
    pensize(20)
    circle(100)
    up()
    bk(100)


done()
