version = 'alpha-0.0.4'


import tkinter as tk
import turtle as tt
import time
from math import sqrt

root = tk.Tk()

root.title("Freefall Motion Simulator "+version)

root.geometry("600x400")

topContainer = tk.Frame(master=root)
topContainer.pack(side=tk.TOP, fill=tk.X)

t = tk.StringVar(value="9.81", name="g")    # Creates var g of class StringVar with value "9.81" amd name "g"

label = tk.Label(master=topContainer, text="g =")
global entry
entry = tk.Entry(master=topContainer, textvariable=t, width=4)    # textvariable=t assigns var t as the constantly updating textvariable for the value of entry
unit = tk.Label(master=topContainer, text="N/kg")
note = tk.Label(master=topContainer, text="1 pixel = 1 metre")
label.pack(side=tk.LEFT, padx=(5,0))
entry.pack(side=tk.LEFT)
unit.pack(side=tk.LEFT)

heightLabel = tk.Label(master=topContainer, text="h =")
f = tk.StringVar(value="100", name="h")
global heightEntry
heightEntry = tk.Entry(master=topContainer, textvariable=f, width=4)
heightUnit = tk.Label(master=topContainer, text="m")
heightLabel.pack(side=tk.LEFT, padx=(5,0))
heightEntry.pack(side=tk.LEFT)
heightUnit.pack(side=tk.LEFT)

bottomContainer = tk.Frame(master=root)
bottomContainer.pack(side=tk.BOTTOM, fill=tk.X)

global e
e = tk.StringVar(value="t = ", name="t")
global timeLabel
timeLabel = tk.Label(master=bottomContainer, textvariable=e)
timeLabel.pack(side=tk.LEFT, padx=(5,0))

global k
k = tk.StringVar(value="v = ", name="v")
global finalVeloLabel
finalVeloLabel = tk.Label(master=bottomContainer, textvariable=k)
finalVeloLabel.pack(side=tk.LEFT, padx=(5,0))

note.pack(side=tk.RIGHT, padx=(0,5))




canvas = tk.Canvas(root)
canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

screen = tt.TurtleScreen(canvas)
global turtle
turtle = tt.RawTurtle(canvas)
turtle.shape("square")
turtle.shapesize(0.5)
turtle.hideturtle()
turtle.up()
turtle.speed(11)
turtle.right(90)

def start():
    e.set("t = ")
    k.set("v = ")
    turtle.speed(5)
    turtle.sety(float(heightEntry.getvar("h"))-210)
    turtle.showturtle()
    turtle.speed(0)

    y = turtle.pos()[1]
    yvel = 0

    debug = time.time()
    while turtle.pos()[1] > -210:
        start = time.time()
        yvel += float(entry.getvar("g"))*0.1
        y -= yvel*0.1
        turtle.sety(y)
        time.sleep(0.1 - (time.time() - start)/20)

    print(time.time() - debug)
    debug1 = time.time() - debug
    turtle.sety(-210)
        
    

    p = e.get()
    p += (str(sqrt(2*float(heightEntry.getvar("h"))/float(entry.getvar("g"))))+' s')
    e.set(p)
    q = k.get()
    q += (str(sqrt(2*(float(entry.getvar("g")))*(float(heightEntry.getvar("h")))))+' m/s')
    k.set(q)

    print(debug1/(sqrt(2*float(heightEntry.getvar("h"))/float(entry.getvar("g")))))

startButton = tk.Button(master=topContainer, text="Run", command=start)
startButton.pack(side=tk.LEFT, padx=(20,0))


root.mainloop()
