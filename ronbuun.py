#Python ronbuun.py
import tkinter as tk
root = tk.Tk()
#フレーム
root.title('Ronbuun')
root.geometry('900x600')

#改行直し前のテキストだよ
txt1 = tk.Text(width=100, height=20)
txt1.pack()

#改行直し後のテキスト
txt2 = tk.Text(width=100, height=20)
txt2.pack()

#メインエンジン
def copy(event):
    ans=""#結果の文
    kazu=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0]
    #一度に読む行数を定義。20行までにしといて
    counta=0
    countb=1
    while(True):
        value=txt1.get(kazu[counta],kazu[countb])#1行目から順に読みこむ
        yomi=value
        ans=ans+yomi
        ans=ans+" "#1行ずつ読み込んだのに半角スペース加えて結果の文に放り込んでる
        counta+=1
        countb+=1
        if(counta==20):#20行まで読ませて止めてる
            break
    ans2=ans.replace('\n','')#何故か改行が残っているので消す
    finans=ans2.replace('- ','')#文字[-1]が何故か機能しないので-を消すために「- 」を指定して消してる
    txt2.delete(1.0,tk.END)#txt2をリセットしておく
    txt2.insert(1.0,finans)#最終的な結果の文を表示
    root.clipboard_clear()#クリップボードをクリア
    root.clipboard_append(finans)#クリップボードにコピー

def setumei(event):
    setumeimado = tk.Toplevel()
    label = tk.Label(setumeimado, text="上のボックスに文章をコピペ(限界20行)してボタンを押すと、改行を直して下のボックスに表示してくれるよ。\n文末の「-」は消してくれるよ。\nついでに結果をクリップボードにコピーまでしてくれるよ。")
    label.pack()

#アプリ起動ボタン
Button = tk.Button(text='押せ！')
Button.bind("<Button-1>",copy)
Button.pack()

#説明書ボタン
Button2 = tk.Button(text='説明書')
Button2.bind("<Button-1>",setumei)
Button2.pack()

root.mainloop()
