print('Hello, world!')  # ②

print('What is your name?')  # 名前を尋ねる
my_name = input()  # ③

print('It is good to meet you, ' + my_name)  # ④

print('The length of your name is:')  # 名前の長さを表示 ⑤
print(len(my_name))

print('What is your age?')  # 年齢を尋ねる ⑥
my_age = input()

print('You will be ' + str(int(my_age) + 1) + ' in a year.')  # 来年の年齢を表示
