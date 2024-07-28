# 3. Write a program that draws some sort of face.

from graphics import *

def main():
    win = GraphWin("Face", 400, 400)
    
    # Head
    head = Circle(Point(200, 200), 100)
    head.setFill("yellow")
    head.draw(win)
    
    # Eyes
    left_eye = Circle(Point(160, 160), 20)
    left_eye.setFill("white")
    left_eye.draw(win)
    
    right_eye = Circle(Point(240, 160), 20)
    right_eye.setFill("white")
    right_eye.draw(win)
    
    # Pupils
    left_pupil = Circle(Point(160, 160), 10)
    left_pupil.setFill("black")
    left_pupil.draw(win)
    
    right_pupil = Circle(Point(240, 160), 10)
    right_pupil.setFill("black")
    right_pupil.draw(win)
    
    # Mouth
    mouth = Oval(Point(150, 250), Point(250, 280))
    mouth.setFill("red")
    mouth.draw(win)
    
    win.getMouse()
    win.close()

main()
