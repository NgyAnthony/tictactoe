from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master=master, width=640, height=400)
        frame.pack()

        self.button1 = Button(frame, width=20, height=5)
        self.button2 = Button(frame, width=20, height=5)
        self.button3 = Button(frame, width=20, height=5)

        self.button4 = Button(frame, width=20, height=5)
        self.button5 = Button(frame, width=20, height=5)
        self.button6 = Button(frame, width=20, height=5)

        self.button7 = Button(frame, width=20, height=5)
        self.button8 = Button(frame, width=20, height=5)
        self.button9 = Button(frame, width=20, height=5)

        self.label = Label(master, text="Hello World")
        self.button_reset = Button(master, text="Reset")
        self.button_quit = Button(master, text="Quit")

        self.button1.grid(row=0, column=0, sticky=NW, pady=2)
        self.button2.grid(row=0, column=1, sticky=N, pady=2)
        self.button3.grid(row=0, column=2, sticky=NE, pady=2)

        self.button4.grid(row=1, column=0, sticky=W, pady=2)
        self.button5.grid(row=1, column=1, pady=2)
        self.button6.grid(row=1, column=2, sticky=E, pady=2)

        self.button7.grid(row=2, column=0, sticky=SW, pady=2)
        self.button8.grid(row=2, column=1, sticky=S, pady=2)
        self.button9.grid(row=2, column=2, sticky=SE, pady=2)

        self.label.pack()
        self.button_reset.pack()
        self.button_quit.pack()

root = Tk()
root.geometry("640x500")
app = App(root)

root.mainloop()
root.destroy() # optional; see description below