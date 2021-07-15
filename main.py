#! python3
# maindd.py - support skillE.py
# 一個の内容に対して小ネタが複数ある。
# 車については小ネタが３個あります。どれを見ますか。
# 使い方についてもしかり。小ネタにも種類がある。
# 使い方に関する小ネタ、車種に関する小ネタ、重要（些細）な小ネタ
# それはおいといてひとまず動くもの
# キーワード検索できる。それで紐づいた情報が見れる。
# 自然な感じで（あいまいな言葉に対しては膨大な情報量が必要。
# キーワード=きーわーど=キー=合言葉
# 情報からも検索できる。使い方に関して検索、一言に関して検索。
# 似た言葉に反応する。→終わりを終わーりたいと打って、終わりですか？と聞く。

# 画像をクリックしたときの処理
#def start():
#    print('ログインしました！')

def init():
    global brainlist
    global title
    path = 'text/brain.txt'
    brainlist=[]

    with open(path,mode='r',encoding='utf-8') as textfile:
        textlinelist = textfile.readlines()

    for textline in textlinelist:
        textlist = textline.replace('\n', '').split(',')
        brainlist.append(textlist)
        #for text in textlist:
        #    brainlist.append(text)
    title = brainlist.pop(0)
    print(brainlist)
    print(title)

init()

while True:
    print('何について調べますか。終わる場合は「終わり」と入力')
    inputvalue = input()
    #print('you say '+inputvalue)
    #if val == 'start' :
    #try:
        #if nasq.index(val) :
    #except ValueError:
    #    pass
    if inputvalue == '終わり':
        break
    if inputvalue == '終わーりたい':
        print('終わりたいんですか？終わる場合は「はい」を入力してください')
        inputvalue = input()
        if inputvalue == 'はい':
            break
        else:
            print('違うんですね')
            continue
    if inputvalue in title:
        index = title.index(inputvalue)
        index = title.index(inputvalue)
        print(title[index]+'について調べます。キーワードを入力してください。')
        inputvalue = input()
        for i in range(len(brainlist)):
            if inputvalue == brainlist[i][0]:
                print(inputvalue+'は'+brainlist[i][index]+'です。')
                #start()
                #break
    else:
        print('それは調べることがらにありません。')
    #    continue
    #break
