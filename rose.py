from turtle import *
list1 = ["purple", "red", "orange", "blue", "green"]

for i in range(200):
    color(list1[i%5])
    pensize(i/10+1)
    forward(i)
    left(59)

done()
