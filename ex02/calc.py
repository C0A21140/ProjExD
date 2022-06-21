from logging import root
import tkinter as tk
import tkinter.messagebox as tkm
def btn_click(event):
    botan = event.widget
    txt = botan["text"]
    #tkm.showinfo("確認", f"[{txt}]ボタンが押されました")
    if txt == "=":
        siki = entry.get()
        kekka = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, kekka)
    else:
        entry.insert(tk.END,txt)

if __name__ == "__main__":
    #ウィンドウの部分
    root = tk.Tk()
    root.title("電卓")

    #ボタンを押したら表示される部分
    entry = tk.Entry(root, justify="right",
                     width = 10,
                      font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 3)

    #ボタンを作る部分
    c = 0
    r = 1
    lt = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "="]
    for i in lt:

        btn = tk.Button(root, text = f"{i}",
                        width = 4, height = 2,
                        font = ("Times New Roman", 30)
                        )
        
        btn.grid(row = r, column = c)
        btn.bind("<1>", btn_click)
        c += 1
        if c == 3:
            r += 1
            c = 0

        
    root.mainloop()
