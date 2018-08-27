import tkinter as tk
import random

class food():
    def __init__(self,cv):
        self.cv = cv
        self.posx = 0
        self.posy = 0
        self.width = 50
    
    def random_pos(self,xmax,ymax):
        self.cv.move(self.brick,-self.posx,-self.posy)
        self.posx = random.randint(0,xmax/self.width-1)*self.width
        self.posy = random.randint(0,ymax/self.width-1)*self.width
        self.cv.move(self.brick,self.posx,self.posy)
    
    def draw_food(self):
        self.brick = self.cv.create_rectangle(self.posx,self.posy,self.posx+self.width,self.posy+self.width,fill="red")

class snake():  #蛇的類別
    def __init__(self,cv,xmax,ymax):
        self.headx = 250
        self.heady = 250
        self.xmax = xmax
        self.ymax = ymax
        self.width = 50
        self.direction = 0
        self.cv = cv
        self.length = 0
        self.body = []

    def draw_body(self):
        tmp = self.cv.create_rectangle(self.headx,self.heady,self.headx+self.width,self.heady+self.width,fill="black")
        self.body.append(tmp)

    def draw_head(self):    #畫出初始的頭
        self.head = self.cv.create_rectangle(self.headx,self.heady,self.headx+self.width,self.heady+self.width,fill="black")

    def turn(self,command):
        self.direction = command

    def update_snake_pos(self):
        if(len(self.body)!=0):
            for i in range(len(self.body)-1,0,-1):
                self.cv.coords(self.body[i],self.cv.coords(self.body[i-1]))
            # print(self.cv.coords(self.body[i]))
            self.cv.coords(self.body[0],self.cv.coords(self.head))
        if(self.direction == 0):
            self.heady = self.heady - self.width
            self.cv.move(self.head,0,-self.width)
            if(self.heady<0):
                self.heady = self.ymax - self.width
                self.cv.move(self.head,0,self.ymax)
        elif(self.direction == 1):
            self.headx = self.headx + self.width
            self.cv.move(self.head,self.width,0)
            if(self.headx >= self.xmax):
                self.headx = 0
                self.cv.move(self.head,-self.xmax,0)
        elif(self.direction == 2):
            self.heady = self.heady + self.width
            self.cv.move(self.head,0,self.width)
            if(self.heady >= self.ymax):
                self.heady = 0
                self.cv.move(self.head,0,-self.ymax)
        elif(self.direction == 3):
            self.headx = self.headx - self.width
            self.cv.move(self.head,-self.width,0)
            if(self.headx<0):
                self.headx = self.xmax - self.width
                self.cv.move(self.head,self.xmax,0)
class game():   #遊戲的類別
    def __init__(self):
        self.root = tk.Tk()
        self.swidth = 500
        self.sheight = 500
        self.cv = tk.Canvas(self.root,width = self.swidth,height = self.sheight,bg="white")
        self.score = 0
        self.score_label = tk.Label(text="score: 0")
        self.cv.pack()
        self.score_label.pack()
        self.sk = snake(self.cv,self.swidth,self.sheight)
        self.sk.draw_head()
        self.fd = food(self.cv)
        self.fd.draw_food()
        self.fd.random_pos(self.swidth,self.sheight)
        self.fps = 12
        self.root.bind("<KeyPress>",self.keydown)
        self.is_gameover = False    
    def keydown(self,e):
        
        if(e.char == 'w'):
            self.sk.turn(0)
        elif(e.char == 'd'):
            self.sk.turn(1)
        elif(e.char == 's'):
            self.sk.turn(2)
        elif(e.char == 'a'):
            self.sk.turn(3)
    
    def start_update_snake_pos(self):
        if(self.is_gameover):
            return
        self.sk.update_snake_pos()
        for i in range(0,len(self.sk.body)-1):
            if(self.cv.coords(self.sk.head) == self.cv.coords(self.sk.body[i])):
                self.is_gameover = True
        if(self.sk.headx == self.fd.posx and self.sk.heady == self.fd.posy):
            self.fd.random_pos(self.swidth,self.sheight)
            self.score += 100
            self.score_label['text'] = "score:" + str(self.score)
            self.sk.draw_body()
        self.root.after(int(1000/self.fps),self.start_update_snake_pos)

    def mainloop(self):
        self.is_gameover = False    
        self.root.mainloop()


newgame = game()
newgame.start_update_snake_pos()
newgame.mainloop()
