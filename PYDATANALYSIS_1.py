# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 22:55:06 2015

@author: Shfun Huang
"""

# NumPy
import numpy as np

# 一維陣列
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

na = np.array(a)
nb = np.array(b)

nc = na*nb
print nc

na[na>=3]

# 二維陣列
na = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
na[0,]
na[1,]

# Transformation Matrix
na.T

# 增添資料的列與行名
na = np.array([['frank', 'M', 29], 
               ['mary', 'F', 23], 
               ['tom', 'M', 35], 
               ['ted', 'M', 33], 
               ['jean', 'F', 21], 
               ['lisa', 'F', 20]])
print na

na = np.array([['name', 'gender', 'age'], 
               ['frank', 'M', 29], 
               ['mary', 'F', 23], 
               ['tom', 'M', 35], 
               ['ted', 'M', 33], 
               ['jean', 'F', 21], 
               ['lisa', 'F', 20]])

# Pandas
import pandas as pd
import time
from random import randint

# 序列(Series)
s = pd.Series([11, 22, 33, 44, 55])
s = pd.Series(range(11,66,11))

# 存取元素與切割 (Indexing & Slicing)
s[2:4]
s[2]

s.max()
s.mean()

# summary
s.describe()

# Data Frame
df = pd.DataFrame([['frank', 'M', 29], 
                   ['mary', 'F', 23], 
                   ['tom', 'M', 35], 
                   ['ted', 'M', 33], 
                   ['jean', 'F', 21], 
                   ['lisa', 'F', 20]])
df.info()

# 新增行名
df.columns=['name', 'gender', 'age']
df
df.describe()

# 存取元素與切割 (Indexing & Slicing)
df[0][:6]

df.ix[1]
df.ix[1:4]
df[['name', 'gender']]

df['gender'] == 'M'
df[df['gender'] == 'M']

# 取男女年齡平均
df[df['gender'] == 'M'].mean()
df[df['gender'] == 'F'].mean()

# SELECT gender, AVERAGE(age) 
# FROM df 
# GROUP BY gender
df.groupby('gender')['age'].mean()

# Data Sets: US Baby Names (1880 - 2010)
# 讀取csv 檔案
names1880 = pd.read_csv('D:/Dropbox/Python/data/yob1880.txt', 
                        names=['name', 'sex', 'births'])
names1880[0:10]
# 5 rows
names1880.head() 
names1880.tail()

# 取性別的標籤類別
names1880['sex'].unique()

# SELECT sex, sum(births)
# FROM names1880
# GROUP BY sex
names1880.groupby('sex')['births'].sum()

# 讀取所有資料做分析
namesall = []
for year in range(1880, 2011):
    time.sleep(randint(1,2))
    try:
        path = 'D:/Dropbox/Python/data/yob' + str(year) + '.txt'
        df = pd.read_csv(path, names=['name', 'sex', 'births'])
        df['year'] = year
        namesall.append(df)
        print path
    except Exception as e:
        print year + ' QQ'
    
# 合併所有資料
df_names = pd.concat(namesall, ignore_index=True)
df_names['year'].unique()

# 統計出每年各性別出生數(births)
# SELECT year, sex, SUM(births)
# FROM df_names
# GROUP BY year, sex
df_names.groupby(['year', 'sex'])['births'].sum().head(10)

# 使用Pivot Table 製作統計表
# 將性別轉成行
table_births = df_names.pivot_table('births', 
                                    rows='year', 
                                    cols='sex', 
                                    aggfunc=sum)
table_births.head(10)

# 使用pandas 的聚合(Aggregation)功能，統計菜市場名排行前十名的名字
names_table = df_names.pivot_table('births', rows='name', aggfunc=sum)
names_table.order(ascending=False).head(10)

# 新增prop 為每年新生兒名字所占該年度的百分比
def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

df_names = df_names.groupby(['year', 'sex']).apply(add_prop)

def get_top(group, n=1000):
    return group.sort_index(by='births', ascending=False)[:n]

grouped = df_names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top)

pieces = []
for year, group in df_names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])

top1000 = pd.concat(pieces, ignore_index=True)
top1000

# 新生兒命名趨勢
total_births = top1000.pivot_table('births',
                                  rows='year',
                                  cols='name',
                                  aggfunc=sum)
total_births.info()

subset = total_births[['John', 'Mary', 'Elizabeth', 'Anna']]
subset.plot(subplots=True,
            figsize=(12,10),
            grid=False,
            title='Number of births per year')

# 命名多樣性 前百名占總新生兒名字的逐年趨勢
prop_table = top1000.pivot_table('prop',
                                rows='year',
                                cols='sex',
                                aggfunc=sum)

prop_table.plot(title='Sum of table100.prop by year and sex',
                xticks=range(1880,2020,10),
                yticks=(0,1))

# Laura Wattenberg　於2007年宣稱男孩子名字最後一個字母的分布在這一百年間有顯著的變化
# 試著用Pandas 證明此一理論
# 統計名字最後一個字的出現次數
df_names['name'].str[-1].head()
# Man only
df_last_letter = df_names#[df_names['sex'] == 'M']
df_last_letter['last_letter'] = df_last_letter['name'].str[-1]
df_last_letter.head(10)

# 每年男性名字尾字統計表
last_letter_table = df_last_letter.pivot_table('births', 
                                               rows='last_letter', 
                                               cols=['sex', 'year'], 
                                               aggfunc=sum)
last_letter_table

# 取樣其中三年的資料
subtable = last_letter_table.reindex(columns=[1999, 2000, 2001], 
                                     level='year')
subtable
letter_prop = subtable / subtable.sum().astype(float)

# Matplotlib plot
import matplotlib.pyplot as plt
table_births.plot(title='Total births by sex and year', figsize=(15, 5))
plt.show() 

# 繪出分布圖
fig, axes = plt.subplots(2, 1, figsize=(10,8))
fig.subplots_adjust(hspace=0.5)
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female')
#fig, axes = plt.subplots(3, 1, figsize=(15,9))
#subtable[1999].plot(kind='bar', rot=0, ax=axes[0], title='1999')
#subtable[2000].plot(kind='bar', rot=0, ax=axes[1], title='2000')
#subtable[2001].plot(kind='bar', rot=0, ax=axes[2], title='2001')

# 繪製在同一張圖上
subtable.plot(kind='bar', rot=0, figsize=(15, 5))

# 把絕對數值轉換成比例
subtable.sum(axis=0)
ratio_subtable = subtable / subtable.sum(axis=0)
ratio_subtable
ratio_subtable.plot(kind='bar', rot=0, figsize=(15, 5))

# 轉換成比例
ratio_table = last_letter_table / last_letter_table.sum(axis=0)
ratio_table

dny = ratio_table.ix[['d', 'n', 'y']].T
dny

# 繪製成折線圖
dny.plot(kind='line', rot=0)

# 男女姓名時空背景差異
# Boy names became girl names (andvice versa)
import numpy as np

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])

lesley_like = all_names[mask]
lesley_like

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()

filtered_table = filtered.pivot_table('births',
                                      rows='year',
                                      cols='sex',
                                      aggfunc='sum')
                                      
filtered_table = filtered_table.div(filtered_table.sum(1),
                                    axis=0)

filtered_table.plot(style={'M':'r-', 'F':'b--'})
