import tkinter
root = tkinter.Tk()

label = tkinter.Label(root,text = "Push Button")
def func():
    label.config(text ="Chaeyoung is the best Twice member")
def myfunc_event(ev):
    label.config(text = "Don't leave me")
button = tkinter.Button(root, text = "Push!!", command = func)
label.pack()
button.pack()
label.bind("<Leave>", myfunc_event)
root.mainloop()
