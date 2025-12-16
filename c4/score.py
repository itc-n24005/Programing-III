# 学生名
students = ["相沢いわし", "伊藤うずら", "上野えのき"]

# 点数リスト
scores = [0, 0, 0]

# インデックス用変数
i = 0

# 点数入力
for name in students:
    scores[i] = int(input(name + "さんの点数を入力してください: "))
    i += 1

# 結果表示
for i in range(len(students)):
    print(students[i], "：", scores[i], "点")
