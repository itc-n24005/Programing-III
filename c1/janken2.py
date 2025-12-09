import random

print("=== じゃんけんゲーム（その２） ===")
print("r: グー, p: パー, s: チョキ, q: 終了\n")

hands = ["r", "p", "s"]
hand_name = {"r": "グー", "p": "パー", "s": "チョキ"}

# 得点
player_score = 0
cpu_score = 0

# 10回勝負
for round in range(1, 11):
    print(f"\n--- {round} 回目 ---")

    # ① コンピュータの手
    cpu = random.choice(hands)

    # ② 人間の手入力
    while True:
        player = input("あなたの手（r/p/s）または q で終了: ")
        if player in ["r", "p", "s", "q"]:
            break
        print("入力が正しくありません。")

    # q → 強制終了 & −1点
    if player == "q":
        print("ゲーム終了を選択したので、あなたのポイントが1点減ります。")
        player_score -= 1
        break

    # ③ 手を表示
    print(f"あなた：{hand_name[player]}  vs  コンピュータ：{hand_name[cpu]}")

    # ④ 勝敗判定
    if player == cpu:
        print("あいこ！ 点数なし")
    elif (player == "r" and cpu == "s") or \
            (player == "s" and cpu == "p") or \
            (player == "p" and cpu == "r"):
        print("あなたの勝ち！ +1点")
        player_score += 1
    else:
        print("コンピュータの勝ち！ +1点")
        cpu_score += 1

# ⑤ 最終結果
print("\n=== 最終結果 ===")
print(f"あなたの点数：{player_score}")
print(f"コンピュータの点数：{cpu_score}")

if player_score > cpu_score:
    print("あなたの勝ちです！🎉")
elif player_score < cpu_score:
    print("コンピュータの勝ちです…")
else:
    print("引き分けです！")

# -----------------------------
# ３．選択ルール：「18」モード
# -----------------------------
print("\n=== 特別ルール：18（イチハチ）モード ===")
print("説明：合計得点が18点以上になったら負け！")
print("あなたとコンピュータが交互に 1〜3 の数字を選んで加算していきます\n")

total = 0  # 現在の合計
turn = "player"  # どちらの番か

while True:
    print(f"\n現在の合計：{total}")

    # プレイヤーのターン
    if turn == "player":
        while True:
            num = input("1〜3 の数字を入力（qで終了）：")
            if num == "q":
                print("ゲーム終了！あなたの負け扱いになります。")
                exit()
            if num in ["1", "2", "3"]:
                num = int(num)
                break
            print("正しく入力してください。")

        total += num

        if total >= 18:
            print(f"合計：{total} → あなたの負け！💣")
            break

        turn = "cpu"

    # コンピュータのターン
    else:
        # CPUはなるべく勝ちやすい戦略を取る
        if total % 4 == 0:
            cpu_num = 3
        else:
            cpu_num = 4 - (total % 4)

        print(f"コンピュータの選んだ数字：{cpu_num}")
        total += cpu_num

        if total >= 18:
            print(f"合計：{total} → コンピュータの負け！🎉")
            break

        turn = "player"

print("\n=== 『18』ゲーム終了 ===")
