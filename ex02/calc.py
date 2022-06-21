from logging import root
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x500")
    c = 0
    r = 0
    for i in range(9, -1, -1):

        btn = tk.Button(root, text = f"{i}",
                        width = 4, height = 2,
                        font = ("Times New Roman", 30)
                        )
        
        btn.grid(row = r, column = c)
        c += 1
        if (i-1)%3 == 0:
            r += 1
            c = 0
    root.mainloop()
