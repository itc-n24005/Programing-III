import random

# 初期スコア
score = 5

# 10回ループの回数をセット
max_try = 10

print("=== 数当てゲーム（その２） ===")
print("0 を入力するとゲーム終了します。")

# 外側ループ（何度もゲーム可能）
while True:
    print(f"\n【現在のスコア: {score}点】")
    print(f"今回のチャレンジ回数: {max_try}回")

    # 内側の数当てループ
    count_success = 0  # 成功回数カウント

    for i in range(max_try):
        # 乱数 1〜10
        answer = random.randint(1, 10)

        # 入力
        user = int(input("1〜10 の数を入力（0で終了）："))

        # 0 ならゲーム終了
        if user == 0:
            print("\n=== ゲーム終了 ===")
            print(f"あなたの最終スコア：{score}点")
            exit()

        # 判定
        if user == answer:
            print("正解！ 🎉")
            score += 10
            count_success += 1

            # 正解するたびにループ回数を1回減らす
            max_try -= 1

            # 10回正解でパーフェクト
            if count_success == 10:
                print("\n★★ パーフェクト達成！！ ★★")
                score += 100
                print(f"最終スコア：{score}点")
                exit()

        else:
            print(f"ハズレ！ 正解は {answer} でした。")
            score -= 1

        # 試行回数がゼロになったら強制終了
        if max_try == 0:
            print("\nループ回数が0になったためゲーム終了。")
            print(f"最終スコア：{score}点")
            exit()

    # 1ゲーム終了後に続けるか？
    print(f"\n１ゲーム終了！現在のスコア：{score}点")
    again = input("続けますか？（y/n）：")
    if again.lower() != "y":
        print("\n=== ゲーム終了 ===")
        print(f"あなたの最終スコア：{score}点")
        break
