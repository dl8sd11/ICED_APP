import tkinter as tk
root =tk.Tk()
label1 = tk.Label(root,text="輸入數字")
label1.grid(row=0,column=0)
Entry1 = tk.Entry(root)
Entry1.grid(row=0,column=1)
button1 = tk.Button(root,text="猜",command=guess)
button1.grid(row=0,column=2)
result_lb = tk.Label(root,text="")
result_lb(row=1,column=0)
root.mainloop()
