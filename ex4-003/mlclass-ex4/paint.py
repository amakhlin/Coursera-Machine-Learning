from Tkinter import *

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None
drawing_area = None;

def callback():
    drawing_area.delete("all")

def main():
    global drawing_area
    root = Tk()

    drawing_area = Canvas(root, width=800, height=800)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)


    b = Button(root, text="clear", command=callback)
    b.pack(side=LEFT)

    root.mainloop()

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def snap(x, y):
    xs = round(float(x)/40.) * 40
    ys = round(float(y)/40.) * 40
    return (xs, ys)

def motion(event):
    if b1 == "down":
        global xold, yold

        #(xold, yold) = snap(xold, yold)
        (xnew, ynew) = snap(event.x, event.y)

        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,xnew,ynew, width=40)
                          # here's where you draw it. smooth. neat.
        xold = xnew
        yold = ynew

if __name__ == "__main__":
    main()