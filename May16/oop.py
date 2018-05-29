#Object Oriented Programming 入門
class slug:
    feet = 0                            #每個slug 都相同的變數Class attributes
    def __init__(self,color=None):      #建構函式
        if color is None:
            self.color = "blue"
        else:
            self.set_color(color)
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color

    @staticmethod                      #每個slug都有一樣的function 不用傳self
    def print_feet():
        print("FATAL ERROR: I have no feet!!!")

    @staticmethod
    def test():
        print("JI")

niceslug = slug("gray")
niceslug.print_feet()
slug.set_color(niceslug,"red")
print(niceslug.get_color())
