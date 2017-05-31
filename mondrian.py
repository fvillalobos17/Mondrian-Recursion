#Felicia Villalobos, Jennifer Kahn
#HW 11/Lab 11: Mondrian Recursion

import random 
from graphics import *

def getrandomColor():
    '''Makes choices of a random color for each square in the painting.'''
    colors = ['Blue', 'Red', 'Yellow','White']
    return (random.choice(colors))

def paintPartition(win,square,depth):
    '''this function creates the recursive aspect of the Mondrian by creating the squares''' 
    depth_max = 6

    p0 = square.getP1()
    x1, y1 = p0.getX(), p0.getY()
    p8 = square.getP2()
    x2, y2 = p8.getX(), p8.getY()
    p1 = Point( (x1 + x2)/2, y1 )
    p2 = Point( x2, y1 )
    p3 = Point( x1, (y1 + y2)/2)
    p4 = Point( (x1 + x2)/2, (y1 + y2)/2 )
    p5 = Point( x2, (y1 + y2)/2 )
    p6 = Point( x1, y2 )
    p7 = Point( (x1 + x2)/2, y2 )

    x = random.randint(0,10)

    if depth >= depth_max:
        return

    if depth < depth_max:
        if x <1:
            square.setFill(getrandomColor())
            return 
 
        else:
            #create 4 squares call paintPartition on all of them
            #making squares with the points

            square1 = Rectangle(p0, p4)
                                
            square2 = Rectangle(p1, p5)
                                
            square3 = Rectangle(p3, p7)
                                
            square4 = Rectangle(p4, p8)
                                
            d1 = [square1,square2,square3,square4]

            for square in d1:
                square.draw(win)
                paintPartition(win,square,depth+1)
                square.setFill(getrandomColor())
                square.setOutline('black')
                square.setWidth(3)
                
         
    
def main():
    win = GraphWin('Mondrian', 500,500)
    win.setBackground('white')
    win.setCoords(-500,-500,500,500)
    x,y = 500,500
    depth = 0
    square = Rectangle(Point(-x,-y),Point(x,y))
    paintPartition(win,square,depth)

    win.getMouse()
    win.close()
                   

main()


 
