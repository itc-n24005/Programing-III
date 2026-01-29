import re

def find_phone_number(text: str):
    # 3桁-4桁-4桁 を探す
    pattern = re.compile(r"\d{3}-\d{4}-\d{4}")
    match = pattern.search(text)
    if match:
        return match.group()
    return None


if __name__ == "__main__":
    s = input("文字列を入力してください（例: 連絡先は090-1234-5678です）: ").strip()

    result = find_phone_number(s)
    if result:
        print("見つかった電話番号:", result)
    else:
        print("電話番号は見つかりませんでした")
