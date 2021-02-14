"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
[コーティングルール]
文字列はダブルコォーテーションで囲うこと

[ファイル説明]
このファイルは冒険ゲームのメインファイルになります。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

game_greeting = "ようこそ！\nこのGameは天才プログラマーが開発した冒険ゲームです。\nぜひ楽しんでください！！１"
question_your_name = "あなたのお名前を教えてください"
question_your_name2 = "空白は入力を受け付けません。もう一度名前を入力してください"
caretaker_talk_1 = "さんって言うのですね。\n素敵なお名前です。早速ですが,Monstorが出てきたので戦ってください！"
caretaker_talk_2 = "敵を倒しました\nこれからも敵がたくさん出てくるので頑張ってください"
battle_talk_1 = "攻撃する場合は大文字の1を入力してください"
battle_talk_2 = "敵に攻撃する！！！！！"
battle_talk_3 = "敵を倒しました！！！！！"
battle_talk_3 = "入力し直してください"

#入力された値が半角、全角の空白かのチェック
def input_cheack_blank():
    while True:
        brave_name = input(question_your_name)
        if(not brave_name):
            print(question_your_name2)
        else:
            break
    return brave_name

#最初の挨拶
#勇者の名前の確認
print(game_greeting)
brave_name = input_cheack_blank()
print(brave_name + caretaker_talk_1)

#勇者の戦闘
while True:
    select = input(battle_talk_1)
    if select == "１":
        print(battle_talk_2)
        print(battle_talk_3)
        break
    else:   
        print(battle_talk_3)

print(caretaker_talk_2)


