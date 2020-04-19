import tkinter as tk

window = tk.Tk()
window.title("Record2Excel")
# height = num * 字體高度1單位
# width = num * 字體長度1單位
# font = ("Arial",字體大小)
# bg = background

Label1 = tk.Label(window, text='hello my name is Leo',
                  height=2,
                  width=20,
                  font=('Arial', 12),
                  bg='red')
Label1.pack()
window.geometry("200x200")
window.mainloop()
