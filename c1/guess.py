import random

# 1. 1〜20 の乱数を発生
r = random.randint(1, 20)

# 当たったかどうかを記録するフラグ
hit = False

# 2. 6 回ループ
for i in range(1, 7):
    n = int(input(f"{i} 回目：数を入力してください → "))

    if n < r:
        print("あなたの推定値は小さいです")
    elif n > r:
        print("あなたの推定値は大きいです")
    else:
        # 一致したらループを抜ける
        hit = True
        break

# 3. 結果表示
if hit:
    print(f"当たり！　{i}回で当てました！")
else:
    print(f"残念！　正解は {r} でした")
