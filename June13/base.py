import tkinter as tk

class snake():  #蛇的類別
    def __init__(self,cv):
        self.headx = 250
        self.heady = 250
        self.width = 50
        self.direction = 1
        self.cv = cv

    def update_pos(self):
        if(self.direction == 0):
            self.cv.move(self.head,0,-self.width)
        elif(self.direction == 1):
            self.cv.move(self.head,self.width,0)
        elif(self.direction == 2):
            self.cv.move(self.head,0,self.width)
        elif(self.direction == 3):
            self.cv.move(self.head,-self.width,0)
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
        self.fps = 5
        self.root.bind("<KeyPress>",self.keydown)
        self.update_snake_pos()
    def update_snake_pos(self):
        self.sk.update_pos()
        self.root.after(int(1000/self.fps),self.update_snake_pos)
    def keydown(self,e):
        print(e.char)
        if(e.char == 'w'):
            self.sk.direction = 0
        elif(e.char == 'd'):
            self.sk.direction = 1
        elif(e.char == 's'):
            self.sk.direction = 2
        elif(e.char == 'a'):
            self.sk.direction = 3

    def mainloop(self):
        self.root.mainloop()


newgame = game()

newgame.mainloop()
