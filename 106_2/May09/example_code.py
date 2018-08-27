import tkinter as tk
import tkinter.messagebox as tkmsg  #彈出視窗moudle
from random import randint


ans = ""  #正確答案
def rand_ans():  #產生合法隨機數字
    global ans  #使用ans全域變數
    rd = randint(1023,9876) #1023~9876的隨機正整數
    while(not(check_input(str(rd),False))):  #檢查是否合法但不輸出警告
        rd = randint(1023,9876)  #如果不合法則重新產生亂數
    ans = str(rd)   #設定Ans
def check_input(input,show_war):
    if input[0] == "0": #檢查首位數字是不是0
        if show_war:
            tkmsg.showwarning("Error", "不能以0開頭")  #彈出警告視窗
        return False
    if not(input.isdigit()) or len(input)!= 4: #檢查是否只為四位數字
        if show_war:
            tkmsg.showwarning("Error", "輸入需為四位數字")  #彈出警告視窗
        return False
    flag=0
    for idx1 in range(len(input)): #檢查數字是否重複
        for idx2 in range(len(input)):
            if idx1!=idx2 and input[idx1]==input[idx2]: #位置不同但是數字相同(也就是重複的意思)
                flag=1
    if flag==1:
        if show_war:
            tkmsg.showwarning("Error", "四數字需全異")
        return False


    return True  #如果前面都沒找到錯誤就回傳正確
def check_ab():
    user_input = guess_entry.get() #取得使用者輸入
    guess_entry.delete(0,tk.END) #清空guess_entry
    if user_input=="": #防止空白猜測
        return
    if not(check_input(user_input,True)): #檢查不合法猜測
        return

    cnt_a = 0
    cnt_b = 0
    for idx1 in range(len(user_input)):
        for idx2 in range(len(ans)):
            if user_input[idx1]==ans[idx2]: #如果答案有一個數字和輸入其中一個數字相同
                if  idx1!=idx2: #位置相同就是A
                    cnt_b += 1
                else:   #否則就是B
                    cnt_a += 1

    result_label.configure(text= str(cnt_a)+'A'+str(cnt_b)+'B')  #設定結果

root =tk.Tk() #宣告主視窗

num_label = tk.Label(root,text="輸入數字") #提示標籤
guess_entry = tk.Entry(root) #使用者的輸入
submit_button = tk.Button(root,text="猜",command=check_ab) #提交答案按鈕
result_label = tk.Label(root,text="",font=('Mono', 54, 'bold'),width="4") #回傳的結果

num_label.grid(row=0,column=0)
guess_entry.grid(row=0,column=1)
submit_button.grid(row=0,column=2)
result_label.grid(row=1,column=0) #把物件排版到視窗上

rand_ans()  #呼叫rand_ans()
root.mainloop()
