from graph import *
def dom(x,y,c):
    brushColor(c)
    rectangle(x, y, x+85, y+375)
    return ()
def car(x,y):
    brushColor('blue')
    rectangle(x, y, x + 85, y + 25)
    rectangle(x+20, y-15, x+20 + 45, y)
penColor(0,0,0)
windowSize (606,858)
brushColor (183,196,200)
rectangle(0, 0, 606, 458)
brushColor (83,108,103)
rectangle(0, 458, 606, 858)
dom(80,100,(147,167,172))
dom(200,115,(147,172,167))
dom(150,135,(183,200,196))
dom(375,100,(219,227,226))
dom(305,205,(111,145,138))
car(100,550)
run()