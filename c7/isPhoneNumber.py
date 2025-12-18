def is_phone_number(text: str) -> bool:
    # 形式: 3桁-4桁-4桁  => 合計 13文字
    if len(text) != 13:
        return False

    # ハイフン位置チェック
    if text[3] != "-" or text[8] != "-":
        return False

    # 数字部分チェック
    part1 = text[0:3]
    part2 = text[4:8]
    part3 = text[9:13]

    if not (part1.isdigit() and part2.isdigit() and part3.isdigit()):
        return False

    return True


if __name__ == "__main__":
    s = input("電話番号を入力してください（例: 090-1234-5678）: ").strip()

    if is_phone_number(s):
        print("電話番号です")
    else:
        print("電話番号ではありません")
