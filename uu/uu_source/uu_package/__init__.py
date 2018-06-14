import xlrd
from tkinter import *
import hashlib       #這是拿來hash運算的可以不需要
import time

LOG_LINE_NUM = 0     #不知道是做什麼的

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #設置窗口
    def set_init_window(self):
        self.init_window_name.title("uu 的 excel 魔法")                          #窗口名
        self.init_window_name.geometry('320x160+10+10')                         #290 160為窗口大小，+10 +10 定義窗口彈出時的默認展示位置
        self.init_window_name["bg"] = "pink"                                    #窗口背景色
        self.init_window_name.attributes("-alpha",0.9)                          #虛化，值越小虛化程度越高

        #按鈕
        self.str_trans_to_md5_button = Button(self.init_window_name, text="我是按鈕", bg="lightblue", width=10) #,command=self.upload_excel可以加這條button功能加進去  # 調用內部方法  加()為直接調用
        self.str_trans_to_md5_button.grid(row=1, column=1)


    #功能函數
    #def upload_excel(self):


def gui_start():
    init_window = Tk()              #實例化出一個父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 設置根窗口默認屬性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口進入事件循環，可以理解為保持窗口運行，否則界面不展示


gui_start()

