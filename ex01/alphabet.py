import random
import datetime
taisyou = 6
kesson = 3
Max = 3
def syutudai():
    alphabet = [chr(c+65) for c in range(26)]

    hyouji = random.sample(alphabet, taisyou)
    print(f"対象文字:{hyouji}")

    kesukazu = random.sample(hyouji, kesson)
    print(f"欠損文字:{kesukazu}")
    for i in range(kesson):
        hyouji.remove(kesukazu[i])
    print(f"表示文字:{hyouji}")

    return kesukazu

def kaitou(x):
    num = int(input("欠損文字はいくつですか:"))
    kotae = []
    if num == len(x):
        print("正解です。では、具体的な文字を入力してください。")
        for i in range(kesson):
            w = input(f"{i+1}つ目の文字を入力してください。:")
            kotae.append(w)
        if set(kotae) == set(x):
            print("正解です。終了します。")
            return 1
        else:
            print("不正解です。もう一度挑戦してください。")
            return 0
    else:
        print("不正解です。")
        return 0
def main():
    st = datetime.datetime.now()
    mondai = syutudai()
    for i in range(Max):
        f = kaitou(mondai)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました。")

if __name__ == "__main__":
    main()

    
    


