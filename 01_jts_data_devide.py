import pandas as pd

FILE_PATH = 'jts_physical_report.xlsx'

OUTPUT_exetra = "output/exetra/"
OUTPUT_cdtn = "output/condition/"
OUTPUT_pscl = "output/physical/"
OUTPUT_msr = "output/measure/"
OUTPUT_frq = "output/frequency/"
OUTPUT_wgt = "output/weight/"

TA_NAME = [
    "森ひかる",
    "高木裕美",
    "櫻井愛菜",
    "田中沙季",
    "増崎セリナ",
    "小野晴茄",
    "澤田守杏",
    "播磨ここね",
    "田中希湖",
    "石田美咲希",
]

df = pd.read_excel(FILE_PATH)

# 01: 関数: 曜日ごとのトレーニング内容

def extract_exetra(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11]]
    df = df[df['名前'] == g_name]
    return df

# 02: 関数: コンディション

def extract_cdtn(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]]
    df = df[df['名前'] == g_name]
    return df

# 04: 関数: フィジカル

def extract_pscl(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 28, 29, 30, 31]]
    df = df[df['名前'] == g_name]
    return df

# 04: 関数: 測定

def extract_msr(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]]
    df = df[df['名前'] == g_name]
    return df

# 05: 関数: トレーニング頻度

def extract_frq(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]]
    df = df[df['名前'] == g_name]
    return df

# 06: 関数: ウエイト

def extract_wgt(FILE_PATH, g_name):
    df = pd.read_excel(FILE_PATH)
    df = df.iloc[:, [2, 3, 1, 63, 64, 65, 66, 67, 68, 69, 70]]
    df = df[df['名前'] == g_name]
    return df

# 01: 曜日ごとのトレーニング内容

for g_name in TA_NAME:
    df = extract_exetra(FILE_PATH, g_name)
    df.to_excel(OUTPUT_exetra+g_name+"_training"+".xlsx", index=False)

# 02: コンディション

for g_name in TA_NAME:
    df = extract_cdtn(FILE_PATH, g_name)
    df.to_excel(OUTPUT_cdtn+g_name+"_condition"+".xlsx", index=False)

# 03: フィジカル

for g_name in TA_NAME:
    df = extract_pscl(FILE_PATH, g_name)
    df.to_excel(OUTPUT_pscl+g_name+"_physical"+".xlsx", index=False)

# 04: 測定

for g_name in TA_NAME:
    df = extract_msr(FILE_PATH, g_name)
    df.to_excel(OUTPUT_msr+g_name+"_measure"+".xlsx", index=False)

# 05: トレーニング頻度

for g_name in TA_NAME:
    df = extract_frq(FILE_PATH, g_name)
    df.to_excel(OUTPUT_frq+g_name+"_frequecy"+".xlsx", index=False)

# 06: ウエイト

for g_name in TA_NAME:
    df = extract_wgt(FILE_PATH, g_name)
    df.to_excel(OUTPUT_wgt+g_name+"_weight"+".xlsx", index=False)


