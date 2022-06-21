from logging import root
import tkinter as tk
import tkinter.messagebox as tkm

#ボタンを押したときの挙動の部分(ゴシックじゃないほう)
def btn_click(event):
    botan = event.widget
    txt = botan["text"]
    if txt == "c":
        entry.delete(0, tk.END)
    elif txt == "=":
        siki = entry.get()
        kekka = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, kekka)
    else:
        entry.insert(tk.END,txt)

#ボタンを押したときの挙動の部分(ゴシック体)
def btn_click2(event):
    botan = event.widget
    txt = botan["text"]
    if txt == "c":
        entry2.delete(0, tk.END)
    elif txt == "=":
        siki = entry2.get()
        kekka = eval(siki)
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, kekka)
    else:
        entry2.insert(tk.END,txt)
    

    

if __name__ == "__main__":
    #ウィンドウの部分
    root = tk.Tk()
    root.title("電卓")

    #ボタンを押したら表示される部分 フォントの違うものを二つ表示
    entry = tk.Entry(root, justify="right",
                     width = 15,
                     font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 4)

    entry2 = tk.Entry(root, justify="right",
                      width = 15,
                      font = ("MSゴシック", 40))
    entry2.grid(row = 1, column = 0, columnspan = 4)

    #ボタンを作る部分
    c = 0
    r = 2
    lt = [7, 8, 9, "+", 4, 5, 6,"-", 1, 2, 3, "*", 0, "c", "/","="]
    for i in lt:

        btn = tk.Button(root, text = f"{i}",
                        width = 4, height = 2,
                        font = ("Times New Roman", 30)
                        )
        
        btn.grid(row = r, column = c)
        btn.bind("<1>", btn_click) #左クリックで通常
        btn.bind("<3>", btn_click2) #右クリックでゴシック体
        c += 1
        if c == 4:
            r += 1
            c = 0

        
    root.mainloop()
