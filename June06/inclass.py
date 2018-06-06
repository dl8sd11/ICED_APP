import tkinter as tk

class snake():  #蛇的類別
    def __init__(self,cv):
        self.headx = 250
        self.heady = 250
        self.width = 50
        self.direction = 0
        self.cv = cv

    def draw_head(self):    #畫出初始的頭
        self.head = self.cv.create_rectangle(self.headx,self.heady,self.headx+self.width,self.heady+self.width,fill="black")

class game():   #遊戲的類別
    def __init__(self):
        self.root = tk.Tk()
        self.swidth = 500
        self.sheight = 500
        self.cv = tk.Canvas(self.root,width = self.swidth,height = self.sheight,bg="white")
        self.cv.pack()
        self.sk = snake(self.cv)
        self.sk.draw_head()
        self.root.bind("<KeyPress>",self.keydown)

    def keydown(self,e):
        print(e.char)
    
    def mainloop(self):
        self.root.mainloop()


newgame = game()

newgame.mainloop()
