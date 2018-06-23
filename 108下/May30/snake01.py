import tkinter as tk

class snake():
    def __init__(self,cv):
        self.cv = cv
        self.headx = 250
        self.heady = 250
        self.width = 30
        self.length = 1
        self.direction = 0
    def start(self):
        self.head = self.cv.create_rectangle(self.headx,self.heady,self.headx+self.width,self.heady+self.width,fill="blue")
    def turn(self,command):
        self.direction = command
        
    def update_snake_pos(self):
        if(self.direction == 0):
            self.heady = self.heady - self.width
            self.cv.move(self.head,0,-self.width)
        elif(self.direction == 1):
            self.headx = self.headx + self.width
            self.cv.move(self.head,self.width,0)
        elif(self.direction == 2):
            self.heady = self.heady + self.width
            self.cv.move(self.head,0,self.width)
        elif(self.direction == 3):
            self.headx = self.headx - self.width
            self.cv.move(self.head,-self.width,0)
class game():
    def __init__(self):
        self.fwidth = 1000
        self.fheight = 1000
        self.root = tk.Tk()
        self.cv = tk.Canvas(self.root,height = self.fheight, width = self.fwidth,bg = "gray")
        self.cv.pack()
        self.sk = snake(self.cv)
        self.sk.start()
        self.fps = 12
        self.root.bind("<KeyPress>",self.keydown)
    def keydown(self,e):
        if(e.char == 'w'):
            self.sk.turn(0)
        elif(e.char == 'd'):
            self.sk.turn(1)
        elif(e.char == 's'):
            self.sk.turn(2)
        elif(e.char == 'a'):
            self.sk.turn(3)
    def update_snake_pos(self):
        self.sk.update_snake_pos()
        self.root.after(int(1000/self.fps),self.update_snake_pos)
    def mainloop(self):
        self.root.mainloop()
    # def update_head(self):
    #     self      

main = game()
main.update_snake_pos()
main.mainloop()