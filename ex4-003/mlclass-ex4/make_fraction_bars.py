from Tkinter import *
import subprocess as sub
import os

canvas_width = 800
canvas_height = 800

def paint_rec(master, x, y, w, h):
	master.create_rectangle(x, y, x+w, y+h)	

master = Tk()
master.title( "Fraction Bars" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)

#w.create_text(50, 50, text='hi')

for row in range(12):
	cur_range = 12 - row;

	for i in range(cur_range):
		paint_rec(w, 100+50*12./cur_range*i, 50 + 60 * row, 50.*12./cur_range, 50)
		if cur_range > 1:
			w.create_text(100+50*12./cur_range*i +  50.*12./cur_range/2., 75 + 60 * row, text='1/%d' % cur_range)
		else:
			w.create_text(100+50.*12./2., 70 + 60 * row, text='1')

    
mainloop()