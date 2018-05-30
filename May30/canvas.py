import tkinter as tk

def move():
    cv.move(rect,10,10)
    root.after(100,move) #after 等待一段時間執行後面function

root = tk.Tk()
cv = tk.Canvas(root,height = 600,width = 800,bg = "white") #畫布
cv.pack()
rect = cv.create_rectangle(50,100,230,400,fill="black") #在畫布上作矩形x1,y1,x2,y2
move()

root.mainloop()