import tkinter as tk

class game:
    def check_win(self):
        if self.board[0]==self.board[1] and self.board[1]==self.board[2] and self.board[0]!='.':
            self.buttons[0]['disabledforeground'] = 'red'
            self.buttons[1]['disabledforeground'] = 'red'
            self.buttons[2]['disabledforeground'] = 'red'

    def button_click(self,x):
        self.buttons[x]['text']=self.now_player
        self.buttons[x]['disabledforeground'] = 'black'
        self.buttons[x]['state'] = 'disabled'
        self.board[x] = self.now_player
        if self.now_player =="X":
            self.now_player = "O"
        else:
            self.now_player = "X"
        self.check_win()

    def __init__(self):
        self.now_player = "X"
        self.root = tk.Tk()
        self.buttons = []
        self.board = []
        for x in range(9):
            button = tk.Button(self.root,font=("Helvetica",32),command=lambda idx=x:  self.button_click(idx),height=1,width=2,text=".")
            button.grid(row=int(x/3),column=x%3)
            self.buttons.append(button)
            self.board.append('.')
    def mainloop(self):
        self.root.mainloop()
newgame = game()
newgame.mainloop()
