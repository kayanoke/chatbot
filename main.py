
# 画像をクリックしたときの処理
def start():
    print('ログインしました！')

path = 'text/brain.txt'
nasq=[]

with open(path,mode='r',encoding='utf-8') as f:
    l = f.readlines()

for name in l:
    las = name.replace('\n', '').split(',')
    for wqwq in las:
        nasq.append(wqwq)

while True:
    print('hello')
    val = input()
    print('you say '+val)
    #if val == 'start' :
    try:
        #if nasq.index(val) :
        if val in nasq:
            start()
            break
    except ValueError:
        pass
