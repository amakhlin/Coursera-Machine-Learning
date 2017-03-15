from Tkinter import *
import subprocess as sub
import os

canvas_width = 800
canvas_height = 800
pixel_size = canvas_width / 40
pen_state = 0
digit_arr = [0 for i in range(400)]
result = None

def paint( event ):
	if(pen_state is 1):
	   #python_green = "#476042"
	   (x, y) = snap(event.x, event.y)
	   x1, y1 = ( x - pixel_size/2 ), ( y - pixel_size/2 )
	   x2, y2 = ( x + pixel_size/2), ( y + pixel_size/2)
	   w.create_rectangle( x1, y1, x2, y2, fill='black')
	   digit_arr[ int(y) / 40 * 19 + int(x) / 40] = 1.

def pendown(event):
	global pen_state
	pen_state = 1

def penup(event):
	global pen_state
	pen_state = 0

def snap(x, y):
    xs = round(float(x)/pixel_size) * pixel_size
    ys = round(float(y)/pixel_size) * pixel_size
    return (xs, ys)

def clear():
	global result
	global digit_arr
	w.delete("all")
	digit_arr = [0 for i in range(400)]
	result.set('')

def rec():
	global result
	f = open('paint_data.m', 'w')
	f.write('digit = [')
	for i in range(20):
		for j in range(20):
			#print '%d' % digit_arr[ i * 19 + j],
			f.write('%f ' % float(digit_arr[ j * 19 + i]))
		#print ''
	#print '\n'
	f.write('];')
	f.close()
	if os.name is not 'nt':
		output = sub.check_output(["octave", "-q", "recognize_digit.m"]);
		result.set('Recognized as: %s' % output.rstrip())


master = Tk()
master.title( "Recognize-a-digit" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<Motion>", paint )

w.bind("<ButtonPress-1>", pendown)
w.bind("<ButtonRelease-1>", penup)

b = Button(master, text="clear", command=clear)
b.pack(side=LEFT)

result = StringVar()
message = Label( master, textvariable=result )
message.pack(side=BOTTOM)

b = Button(master, text="recognize", command=rec)
b.pack(side=RIGHT)
    
mainloop()