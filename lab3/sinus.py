from graph import *

penColor(255,0,255)
penSize(5)
def s(x):
    y=x+x*x+200
    return y
for i in range (1,5000):
    a=s(i)
    point(i,a)
run()