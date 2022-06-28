import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as make
def key_down(event):
    global key
    key = event.keysym
    #tkm.showinfo("キー押下", f"{key}が押されました")

def key_up(event):
    global key
    key = ""
    tori["file"] = "fig/0.png"

def main_proc():
    global cx, cy, mx, my, tori, canvas
    if key == "Up":
        if meiro[my-1][mx] == 0:
            tori["file"] = "fig/6.png"
            my -= 1
    elif key == "Down":
        if meiro[my+1][mx] == 0:
            tori["file"] = "fig/8.png"
            my += 1
    elif key == "Right":
        if meiro[my][mx+1] == 0:
            tori["file"] = "fig/2.png"
            mx += 1
    elif key == "Left":
        if meiro[my][mx-1] == 0:
            tori["file"] = "fig/3.png"
            mx -= 1
    cx, cy = mx*100+50, my*100+50
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
    meiro = make.make_maze(15, 9)
    byouga = make.show_maze(canvas, meiro)
    mx, my = 1, 1
    tori = tk.PhotoImage(file = "fig/0.png")
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    root.mainloop()