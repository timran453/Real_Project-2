from turtle import *


# bgcolor("#123456")

#Center circle
color("#202020")
up()
goto(0,-50)
down()
begin_fill()
fillcolor("#ff0000")
circle(50)
end_fill()
up()
home()


# X, Y circle
color("#00ff00")
goto(150,150)
down()
begin_fill()
fillcolor("#f0f050")
circle(50)
end_fill()
up()
home()



# -X, Y circle
color("#ff0000")
goto(-150,150)
down()
begin_fill()
fillcolor("#00ff00")
circle(50)
end_fill()
up()
home()



# -X, -Y circle
color("#908070")
goto(-200,-200)
down()
begin_fill()
fillcolor("#0000ff")
circle(50)
end_fill()
up()
home()



# X, -Y circle
color("#654321")
goto(200,-200)
down()
begin_fill()
fillcolor("#f020a0")
circle(50)
end_fill()
up()
home()
down()








# hideturtle()
done()
