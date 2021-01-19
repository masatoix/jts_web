import streamlit as st
import pandas as pd
import plotly.express as px
import plotly
import openpyxl


input_file_cnd = 'output/condition/'
input_file_phy = 'output/physical/'
input_file_exe = 'output/exetra/'
input_file_frq = 'output/frequency/'
input_file_msr = 'output/measure/'

"""
# 次世代ターゲット事業
## `測定データベース`
___
"""

ta_name = st.sidebar.selectbox("ターゲットアスリート名を選択", (
    "森ひかる",
    "高木裕美",
    "櫻井愛菜",
    "田中沙季",
    "増崎セリナ",
    "小野晴茄",
    "澤田守杏",
    "播磨ここね",
    "田中希湖",
    "石田美咲希",))

"""
### 身長・体重
"""

if ta_name == ta_name:
    df = pd.read_excel(input_file_phy+ta_name+'_physical.xlsx')
    st.dataframe(df.style.highlight_max(axis=0), height=1000)

    if st.checkbox('身長・体重: グラフを表示'):
        st.write(
        px.bar(df, x='レポート月', y='身長', height=400)
        )
        st.write(
            px.bar(df, x='レポート月', y='RH幅', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体重', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体脂肪率', height=400)
        )

"""
### コンディション
"""

if ta_name == ta_name:
    df = pd.read_excel(input_file_cnd+ta_name+'_condition.xlsx')
    st.dataframe(df.style.highlight_max(axis=0), height=1000)

    if st.checkbox('コンディション: グラフを表示'):
        st.write(
            px.bar(df, x='レポート月', y='心拍数', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体温',  height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='SPO2', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体調 [疲労感]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体調 [倦怠感]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体調 [食欲]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体調 [今の体調]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体調 [意欲]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [首の痛み]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [肩の痛み]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [背中の痛み]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [腰の痛み]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [下腿部の痛み]', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケガなど [足部の痛み]', height=400)
        )

"""
### トレーニング頻度
"""
if ta_name == ta_name:
    df = pd.read_excel(input_file_exe+ta_name+'_training.xlsx')
    st.dataframe(df.style.highlight_max(axis=0), height=1000)

"""
### トレーニング種目の頻度
"""
if ta_name == ta_name:
    df = pd.read_excel(input_file_frq+ta_name+'_frequecy.xlsx')
    st.dataframe(df.style.highlight_max(axis=0), height=1000)

    if st.checkbox('トレーニング種目の頻度: グラフを表示'):
        st.write(
        px.bar(df, x='レポート月', y='サーキット', height=400)
        )
        st.write(
            px.bar(df, x='レポート月', y='Power Max 耐乳酸', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='Power Max パワー', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='メディシンボール', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ケトルベル', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='自重バランス', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体幹クッション (青)', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='体幹バランス (赤)', height=400)
        )
        st.write(
        px.bar(df, x='レポート月', y='体幹バランス (ハーフカット)', height=400)
        )
        st.write(
            px.bar(df, x='レポート月', y='BOSSバランス', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ウォーターバッグ', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ウォーターボール', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='倒立バー', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='バレエ', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='フレックスクッション', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='ストレッチポール', height=400)
        )
        st.write(
        px.bar(df, x='レポート月', y='フロッグバンド', height=400)
        )
        st.write(
            px.bar(df, x='レポート月', y='チューブ', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='バンド', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='エスパージ (低周波道パルス)', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='交代浴', height=400)
        )
        
"""
### パフォーマンス測定
"""

if ta_name == ta_name:
    df = pd.read_excel(input_file_msr+ta_name+'_measure.xlsx')
    st.dataframe(df.style.highlight_max(axis=0), height=1000)

    if st.checkbox('パフォーマンス測定: グラフを表示'):
        st.write(
        px.line(df, x='レポート月', y='立ち幅跳びー脚', height=400)
        )
        st.write(
            px.bar(df, x='レポート月', y='立ち幅跳びー全身', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='倒立 (秒)', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='閉眼片足 右 (秒) ', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='閉眼片足 (左)', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='バックスクラッチ 右が上', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='バックスクラッチ 左が上', height=400)
        )
        st.write(
            px.line(df, x='レポート月', y='20本ジャンプ (秒)', height=400)
        )

"""
 
## `データ比較`
---
### 20本ジャンプ比較
"""

df = pd.read_excel('compare/jump.xlsx')
st.write(df.style.highlight_max(), axis=0)
st.write(
    px.line(df, title='20本ジャンプ秒数の推移',
    x='レポート月', 
    y=[
        "森ひかる",
        "高木裕美",
        "櫻井愛菜",
        "田中沙季",
        "増崎セリナ",
        "小野晴茄",
        "澤田守杏",
        "播磨ここね",
        "田中希湖",
        "石田美咲希"
    ], 
        width=800, 
        height=600,
        )
)

"""
# 第57回全日本トランポリン競技選手権大会
---
## 女子 第2自由演技
"""

df = pd.read_excel('compare/test.xlsx')
st.write(df.style.highlight_max(), axis=0)

st.write(
    px.scatter(df, x='D-score', y='E-score', size='Flight', color='age', log_x=True, size_max=15)
)


# ta_names = [
#     "森ひかる",
#     "高木裕美",
#     "櫻井愛菜",
#     "田中沙季",
#     "増崎セリナ",
#     "小野晴茄",
#     "澤田守杏",
#     "播磨ここね",
#     "田中希湖",
#     "石田美咲希",
# ] 

# def webdata_msr(df):
#     st.write(
#     px.bar(df, x='レポート月', y='立ち幅跳び ー 脚 (例: 2.1m)', height=400)
#     )
#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 全身 (例: 1.85m)', height=400)
#     )
#     st.write(
#         px.line(df, x='レポート月', y='倒立 (秒)', height=400)
#     )
#     st.write(
#         px.line(df, x='レポート月', y='閉眼片足 右 (秒) ', height=400)
#     )
#     st.write(
#         px.line(df, x='レポート月', y='閉眼片足 (左)', height=400)
#     )
#     st.write(
#         px.line(df, x='レポート月', y='20本ジャンプ (秒)', height=400)
#     )

# for g_name in ta_names:
#     if　st.checkbox(g_name + 'のデータを表示'):
#         df = pd.read_excel('output/measure/'+g_name+'_measure.xlsx')
#         st.dataframe(df.style.highlight_max(axis=0), height=1000)
#         webdata_msr(df)



# """
# # 石田美咲希
# ## パフォーマンス測定
# """

# df = pd.read_excel('output/石田美咲希_measure_test.xlsx')
# st.dataframe(df.style.highlight_max(axis=0), height=1000)

# # des_list = df['month'].unique()

# # selected_des = st.sidebar.selectbox(
# #     '表示する種目を選択',
# #     des_list
# # )

# # df = df[df['month']==selected_des]

# if st.checkbox('グラフを表示'):
#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 脚 (例: 2.1m)', height=400)
#     )

#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 全身 (例: 1.85m)', height=400)
#     )

#     st.write(
#         px.line(df, x='レポート月', y='倒立 (秒)', height=400)
#     )

#     st.write(
#         px.line(df, x='レポート月', y='閉眼片足 右 (秒) ', height=400)
#     )

#     st.write(
#         px.line(df, x='レポート月', y='閉眼片足 (左)', height=400)
#     )

#     st.write(
#         px.line(df, x='レポート月', y='20本ジャンプ (秒)', height=400)
#     )

# """
# # 田中希湖
# ## パフォーマンス測定
# """

# df = pd.read_excel('output/石田美咲希_measure_test.xlsx')
# st.dataframe(df.style.highlight_max(axis=0), height=1000)

# dataset_name = st.selectbox("Select Dataset", ("立ち幅跳びー脚", "立ち幅跳びー全身", "倒立", "20本ジャンプ"))
# # st.write(dataset_name)

# if dataset_name == '立ち幅跳びー脚':
#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 脚 (例: 2.1m)', height=400)
#     )
# elif dataset_name == '立ち幅跳びー全身':
#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 全身 (例: 1.85m)', height=400)
#     )
# elif dataset_name == '倒立':
#     st.write(
#         px.line(df, x='レポート月', y='倒立 (秒)', height=400)
#     )

# elif dataset_name == '20本ジャンプ':
#     st.write(
#         px.line(df, x='レポート月', y='20本ジャンプ (秒)', height=400)
#     )

# """
# # 田中希湖
# ## パフォーマンス測定
# """

# df = pd.read_excel('output/石田美咲希_measure_test.xlsx')
# st.dataframe(df.style.highlight_max(axis=0), height=1000)



#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 脚 (例: 2.1m)', height=400)
#     )
# elif dataset_name == '立ち幅跳びー全身':
#     st.write(
#         px.bar(df, x='レポート月', y='立ち幅跳び ー 全身 (例: 1.85m)', height=400)
#     )
# elif dataset_name == '倒立':
#     st.write(
#         px.line(df, x='レポート月', y='倒立 (秒)', height=400)
#     )

# elif dataset_name == '20本ジャンプ':
#     st.write(
#         px.line(df, x='レポート月', y='20本ジャンプ (秒)', height=400)
    # )