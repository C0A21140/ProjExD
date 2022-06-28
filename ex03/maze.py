import tkinter as tk
import tkinter.messagebox as tkm
def key_down(event):
    global key
    key = event.keysym
    #tkm.showinfo("キー押下", f"{key}が押されました")

def key_up(event):
    global key
    key = ""
    
def main_proc():
    global cx, cy, key
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Right":
        cx += 20
    elif key == "Left":
        cx -= 20
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,
                       width = 1500,
                       height = 900,
                       bg = "black"
                       )
    canvas.pack()
    tori = tk.PhotoImage(file = "fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    root.mainloop()