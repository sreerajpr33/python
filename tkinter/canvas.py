import tkinter 
app=tkinter.Tk()
c=tkinter.Canvas(app,width=400,height=400,bg="sky blue")
c.create_line(0,150,350,150,fill="black")
c.create_rectangle(50,50,350,250,fill="yellow")
c.create_oval(50,50,350,250,fill="orange")
c.pack()
app.mainloop()