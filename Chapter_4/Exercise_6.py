# 6. Modify the graphical future value program so that the input (principal and apr) also are done
#    in a graphical fashion using Entry objects.

from graphics import *

def main():
    # Create a graphics window for input
    input_win = GraphWin("Investment Input", 400, 300)
    input_win.setBackground("light gray")
    input_win.setCoords(0, 0, 300, 200)
    
    # Add input fields for principal and apr
    Text(Point(80, 150), "Initial Principal:").draw(input_win)
    principal_entry = Entry(Point(200, 150), 10)
    principal_entry.setText("0.0")
    principal_entry.draw(input_win)
    
    Text(Point(80, 100), "Annual Interest Rate:").draw(input_win)
    apr_entry = Entry(Point(200, 100), 10)
    apr_entry.setText("0.0")
    apr_entry.draw(input_win)
    
    # Add a button to submit the input
    submit_button = Text(Point(150, 50), "Submit")
    submit_button.draw(input_win)
    Rectangle(Point(120, 30), Point(180, 70)).draw(input_win)
    
    # Wait for a mouse click to get input
    input_win.getMouse()
    
    # Retrieve values from input fields
    principal = float(principal_entry.getText())
    apr = float(apr_entry.getText())
    
    # Close the input window
    input_win.close()
    
    # Create a graphics window for the investment growth chart
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    
    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
    # Wait for user to close the window
    win.getMouse()
    win.close()

main()

