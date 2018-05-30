import tkinter as tk

class game():
    def __init__(self):
        self.root = tk.Tk()
        self.swidth = 500
        self.sheight = 500
        self.cv = tk.Canvas(self.root,width = self.swidth,height = self.sheight,bg="white")
        self.cv.pack()
    def mainloop(self):
        self.root.mainloop()
    def draw_rect(self):
        self.cv.create_rectangle(10,10,200,200,fill = "black")

newgame = game()
newgame.draw_rect()
newgame.mainloop()
