# あいさつ（課題版）

# (1) 名前を入力
name = input("名前を入力してください：")

# (2) 時間帯を数値で入力
print("時間帯を選んでください")
print("1：朝　2：昼　3：晩　4：寝る前")
time = int(input("番号を入力してください："))

# (3) 時間帯によってあいさつを切り替える
if time == 1:
    print(f"{name}さん、おはようございます")
elif time == 2:
    print(f"{name}さん、こんにちは")
elif time == 3:
    print(f"{name}さん、こんばんは")
elif time == 4:
    print(f"{name}さん、おやすみなさい")
else:
    print("正しい番号を入力してください")
