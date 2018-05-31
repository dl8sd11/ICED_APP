import tkinter as tk

class snake():
    def __init__(self,cv):
        self.headx = 250
        self.heady = 250
        self.width = 50
        self.direction = 0
        self.cv = cv

    def draw_head(self):
        self.cv.create_rectangle(self.headx,self.heady,self.headx+self.width,self.heady+self.width,fill="black")

class game():
    def __init__(self):
        self.root = tk.Tk()
        self.swidth = 500
        self.sheight = 500
        self.cv = tk.Canvas(self.root,width = self.swidth,height = self.sheight,bg="white")
        self.cv.pack()
        self.sk = snake(self.cv)
        self.sk.draw_head()
    def mainloop(self):
        self.root.mainloop()


newgame = game()

newgame.mainloop()
