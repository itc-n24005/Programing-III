import random

# 1. 勝ち・負け・あいこの初期化
win = 0
lose = 0
draw = 0

# 手の対応表
hands = {"r": "グー", "p": "パー", "s": "チョキ"}

while True:
    # (1) 勝敗数表示
    print("\n--- 現在の成績 ---")
    print(f"勝ち：{win}   負け：{lose}   あいこ：{draw}\n")

    # (2) プレイヤー入力ループ
    while True:
        player = input("r(グー) / p(パー) / s(チョキ) / q(終了) を入力してください → ")

        if player == "q":
            print("ゲーム終了します。")
            exit()    # プログラム終了

        if player in ["r", "p", "s"]:
            break

        print("※ r, p, s, q のいずれかを入力してください。")

    # (3) プレイヤーの手を表示
    print(f"あなた：{hands[player]}")

    # (4) コンピュータの手（ランダム）
    comp = random.choice(["r", "p", "s"])

    # (5) コンピュータの手を表示
    print(f"コンピュータ：{hands[comp]}")

    # (6) 判定
    if player == comp:
        result = "あいこ！"
        draw += 1
    elif (player == "r" and comp == "s") or \
         (player == "s" and comp == "p") or \
         (player == "p" and comp == "r"):
        result = "あなたの勝ち！"
        win += 1
    else:
        result = "あなたの負け！"
        lose += 1

    print("→ 結果：" + result)
