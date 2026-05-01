import datetime
import unicodedata
import re

# 各年号の元年を定義
eraDict = {
    "明治": 1868,
    "大正": 1912,
    "昭和": 1926,
    "平成": 1989,
    "令和": 2019,
}

# 和暦から西暦への変換関数
def japanese_calendar_converter(text):
    # 正規化
    normalized_text = unicodedata.normalize("NFKC", text)

    # 年月日を抽出
    pattern = r"(?P<era>{eraList})(?P<year>[0-9]{{1,2}}|元)年".format(eraList="|".join(eraDict.keys()))
    date = re.search(pattern, normalized_text)

    # 抽出できなかったらエラーを返す
    if date is None:
        print("和暦を変換できません")
        return None

    # 年を変換
    for era, startYear in eraDict.items():
        if date.group("era") == era:
            if date.group("year") == "元":
                year = eraDict[era]
            else:
                year = eraDict[era] + int(date.group("year")) - 1
            return datetime.date(year, 1, 1)  # 日付を1月1日として返す

# 西暦を和暦に変換する関数
def to_japanese_era(year):
    for era, start_year in reversed(eraDict.items()):
        if year >= start_year:
            return f"{era}{year - start_year + 1}年度"
    return f"西暦{year}年度"

# 年度計算（早生まれ対応）
def calculate_graduation_year(birth_year, early_birth):
    # 学校の開始年度を計算（早生まれなら1年後ろにずらす）
    if early_birth:
        birth_year += 1

    school_years = {
        "小学校": birth_year + 12,
        "中学校": birth_year + 15,
        "高校": birth_year + 18,
    }

    return school_years

# 確認プロセス
def ask_progress():
    # 生まれ年を確認
    birth_year_input = input("生まれた年を西暦か和暦で入力してください: ")
    
    # 西暦か和暦で判定して変換
    if birth_year_input.isdigit():
        birth_year = int(birth_year_input)
    else:
        birth_year = japanese_calendar_converter(birth_year_input).year

    # 早生まれかどうかを確認
    early_birth = input("あなたは早生まれですか？ (はい/いいえ): ").lower() == "はい"
    
    # 各卒業年度の計算
    graduation_years = calculate_graduation_year(birth_year, early_birth)

    # 中学卒業後の進路確認
    print(f"小学校: {graduation_years['小学校']}年度 ({to_japanese_era(graduation_years['小学校'])})")
    print(f"中学校: {graduation_years['中学校']}年度 ({to_japanese_era(graduation_years['中学校'])})")
    print(f"高校: {graduation_years['高校']}年度 ({to_japanese_era(graduation_years['高校'])})")
    high_school = input("高校卒業後はどうしましたか？ (大学/短大/就職/高校を中退している): ")

    if high_school == "大学":
        university_type = input("大学は何年制ですか？ (4年/医学部6年): ")
        if university_type == "4年" or 4:
            uni_graduation = graduation_years['高校'] + 4
            print(f"大学: {uni_graduation}年度 ({to_japanese_era(uni_graduation)})")
        elif university_type == "医学部6年" or 6:
            med_graduation = graduation_years['高校'] + 6
            print(f"医学部: {med_graduation}年度 ({to_japanese_era(med_graduation)})")

    elif high_school == "短大":
        junior_college_graduation = graduation_years['高校'] + 2
        print(f"短大: {junior_college_graduation}年度 ({to_japanese_era(junior_college_graduation)})")

    elif high_school == "中退":
        dropout_year = graduation_years['中学校']+int(input("何年に中退しましたか？: "))
        print(f"高校中退: {dropout_year}年度 ({to_japanese_era(dropout_year)})")

    # 大学院の確認
    if high_school == "大学":
        grad_school = input("大学院に進学しましたか？ (はい/いいえ): ")
        if grad_school == "はい":
            grad_school_years = int(input("大学院は何年制ですか？ (修士2年/博士3年): "))
            grad_school_graduation = uni_graduation + grad_school_years
            print(f"大学院: {grad_school_graduation}年度 ({to_japanese_era(grad_school_graduation)})")
    
    print("おしまい")

ask_progress()