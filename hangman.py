import random

def hangman(word):
    wrong = 0
    stage = ["",
             "________        ",
             "l               ",
             "l       l       ",
             "l       0       ",
             "l      /l?      ",
             "l      / ?      ",
             "l               ",
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

    while wrong < len(stage) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong+1
        print("\n".join(stage[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(board))
        print("あなたの負け！正解は{}.".format(word))

word =['aaa','bbb','ccc']
hangman(word[random.randint(0,2)])            
