# 数占い（基本版）

# 1. 生年月日を文字列で入力
year = input("生まれた年を入力してください：")
month = input("生まれた月を入力してください：")
day = input("生まれた日を入力してください：")

# 生年月日をまとめる
birthday = year + month + day

# 2. 1桁ずつ取り出して合計
total = 0
for ch in birthday:
    total += int(ch)

# 3. 1桁になるまで繰り返し足す
while total >= 10:
    temp = 0
    for ch in str(total):
        temp += int(ch)
    total = temp

# 4. 結果表示
print(f"あなたの運命数は {total} です")
