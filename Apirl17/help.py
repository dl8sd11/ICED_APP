# GUI模組
import tkinter as tk
import tkinter.messagebox as tkmsg

root = tk.Tk()

# 一段文字

Label1 = tk.Label(root,text = "test",font=("font-family",font-size,"styles"))
Label1.grid(row = y,column = x)

# 輸入框
Entry1 = tk.Entry(root)
Entry1.grid(row=y,column=x)
print(Entry1.get())

#按鈕
def foo():
    do_something()
Button1 = tk.Button(root,text="iambtn",command=foo)
Button1.grid(row=y,column=x)

# 鍵盤偵測
def key(event):
    print(event.char)
root.bind("<Key>",key)


root.mainloop()
