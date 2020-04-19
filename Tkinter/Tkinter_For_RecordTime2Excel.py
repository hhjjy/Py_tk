import tkinter as tk
import time
# todo : initial all
window = tk.Tk()
Var = tk.StringVar()
window.title("Record2Excel")
on_Click = True
def click_me():
    global on_Click
    if on_Click:
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        Var.set(t)
        on_Click = not on_Click
    else:
        Var.set("Stop")
        on_Click = not on_Click
# todo : Button Setting tips
# height = num * 字體高度1單位
# width = num * 字體長度1單位
# font = ("Arial",字體大小)
# bg = background
# Var =  tk.StringVar()    # 文字可以改變 文字除存器

Label1 = tk.Label(window, textvariable=Var,
                  height=2,
                  width=20,
                  font=('Arial', 12),
                  bg='red')
# todo : Button Setting tips
# text='hit me',      # 显示在按钮上的文字
# command=hit_me     # 点击按钮式执行的命令
Button1 = tk.Button(window, text="Start Counting",
                    height=2,
                    width=15,
                    font=("Arial", 12),
                    bg="white",
                    command=click_me
                    )
Label1.pack()
Button1.pack()
window.geometry("200x200")
window.mainloop()
