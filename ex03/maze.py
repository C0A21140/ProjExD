import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    window = tk.Canvas(root,
                       width = 1500,
                       height = 900,
                       bg = "black")
    window.pack()
    root.mainloop()