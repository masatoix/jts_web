# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import streamlit as st
import pandas as pd
import plotly.express as px
from glob import glob


# %%
# TA_NAMES = [
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

input_file = 'output/measure/'
output_file = 'compare/'


# %%
file_paths = glob(input_file+'*.xlsx')
file_paths


# %%
def extract(file_path):
    df = pd.read_excel(file_path)
    column = df.iloc[0, 2]
    df = df.iloc[:, [1, 12]]
    df = df.rename(columns={'20本ジャンプ (秒)':column})
    return df


# %%
df = pd.DataFrame()

for file_path in file_paths:
    df = pd.concat([df, extract(file_path)], axis=1)


# %%
df = df.iloc[:, [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]
df.to_excel(output_file+'jump.xlsx', index=False)


# %%
df