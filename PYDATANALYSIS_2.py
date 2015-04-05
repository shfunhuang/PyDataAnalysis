# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 23:25:30 2015

@author: Shfun Huang
"""

# Pylab Interface
import pylab
import numpy as np

pylab.plot?
%pylab inline

# Figure and Axes
import matplotlib.pyplot as plt

fig = plt.figure()  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)

# 繪製多張圖
fig = plt.figure()
for i in range(6):
    ax = fig.add_subplot(2, 3, i + 1)
    ax.set_title("Plot #%i" % i)

# Grid 系統
fig = plt.figure(figsize=(8, 8))
gss = plt.GridSpec(3, 3)
ax1 = fig.add_subplot(gss[0, :])  # 第1列全
ax2 = fig.add_subplot(gss[1, :2]) # 第1列第2行前全部
ax3 = fig.add_subplot(gss[1:, 2]) # 第2行第1列後全部
ax4 = fig.add_subplot(gss[2, 0])
ax5 = fig.add_subplot(gss[2, 1])

# 折線圖 Line Chart
x =[2,5,10] 
y =[1,3,9]
pylab.plot(x, y)
pylab.plot(x, y, '-r') # color: red

# 同時畫出兩條線
x1 =[2,5,10] 
y1 =[1,3,9]

x2 =[1,3,8] 
y2 =[5,2,7]

pylab.plot(x1, y1)
pylab.plot(x2, y2, '-r') #red solid line

# 增加label
pylab.plot(x1, y1, '--r', label="google") # red dashed line 
pylab.plot(x2, y2, label="amazon")
pylab.legend()

# 標記位置 (line style)
pylab.plot(x1, y1, '^') # filled triangles
pylab.plot(x1, y1, ':r' ,label="amazon") # red dotted line
pylab.legend()

# 調整間距 (xlim, ylim)
pylab.plot(x1, y1, 'bo')
pylab.plot(x1, y1, ':k' ,label="amazon")
pylab.legend()
pylab.xlim(0,12)
pylab.ylim(0,12)

# 增加Title 與tick label
pylab.plot(x1, y1, 'bo')
pylab.plot(x1, y1, ':k' ,label="amazon")
pylab.legend()
pylab.xlim(0,12)
pylab.ylim(0,12)
pylab.xlabel('this is x!')
pylab.ylabel('this is y!')
pylab.title('My Plot')

# 長條圖 barplot
fig, ax = plt.subplots()
x = [2,3,4,5,5,5,3,5,7,9]
n, bins, patches = ax.hist(x, 20, normed=0, histtype='bar')

# 將圖表做 Normalization
fig, ax = plt.subplots()
x = [2,3,4,5,5,5,3,5,7,9]
n, bins, patches = ax.hist(x, 20, normed=1, histtype='bar')

# Step Bar 圖
fig, ax = plt.subplots()
x = [2,3,4,5,5,5,3,5,7,7,9,9,9, 4, 4]
n, bins, patches = ax.hist(x, 20, normed=1, histtype='step')

# 繪製兩份 Bar 在同一張圖上
fig, ax = plt.subplots()
x1 = [2,3,4,5,5,5,3,5,7,9]
x2 = [1,1,1,2,2,5,7,7,7,9,10]
n, bins, patches = ax.hist(x1, 20, normed=1, histtype='bar')
n, bins, patches = ax.hist(x2, 20, normed=1, histtype='bar')

# 增加透明度
fig, ax = plt.subplots()
x1 = [2,3,4,5,5,5,3,5,7,9]
x2 = [1,1,1,2,2,5,7,7,7,9,10]
n, bins, patches = ax.hist(x1, 20, normed=1, histtype='bar')
n, bins, patches = ax.hist(x2, 20, normed=1, histtype='bar', alpha=0.5)

# 並列成圖
x1 = [2,3,4,5,5,5,3,5,7,9]
x2 = [1,1,1,2,2,5,7,7,7,9,10]

fig, ax = plt.subplots()
n, bins, patches = ax.hist( [x1,x2], 10,  histtype='bar')


# 大餅圖 Pie Chart
fracs = [30, 15, 45, 10]
colors = ['b', 'g', 'r', 'w']
fig, ax = plt.subplots(figsize=(6, 6))  # make the plot square
pie = ax.pie(fracs, colors=colors, explode=(0, 0, 0.05, 0), shadow=True,
             labels=['Apple', 'Google', 'Dropbox', 'Amazon'])

# 散佈圖 Scatter plot
x = [1,2,3]
y = [-1,10,5]
s = [1000,2000,3000]

fig, ax = plt.subplots()
im = ax.scatter(x, y, s=s, cmap=plt.cm.jet)

# 為散佈圖增添點顏色
fig, ax = plt.subplots()
im = ax.scatter(x, y, c=['r', 'g', 'b'], s=s, cmap=plt.cm.jet)

# Pygal
import pygal 

bar_chart = pygal.Bar()                                            
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  
bar_chart.render_to_file('./svg/bar_chart.svg') 

from IPython.display import SVG
SVG(filename='./svg/bar_chart.svg')

# 繪製多張圖
bar_chart = pygal.Bar()
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file('./svg/bar_chart2.svg') 
SVG(filename='./svg/bar_chart2.svg')

# 橫向直方圖
bar_chart = pygal.HorizontalStackedBar()
bar_chart.title = "Remarquable sequences"
bar_chart.x_labels = map(str, range(11))
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file('./svg/bar_chart3.svg') 
SVG(filename='./svg/bar_chart3.svg')

# 圓餅圖
multipie_chart = pygal.Pie()
multipie_chart.title = 'Browser usage by version in February 2012 (in %)'
multipie_chart.add('IE', [5.7, 10.2, 2.6, 1])
multipie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
multipie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
multipie_chart.add('Safari', [4.4, .1])
multipie_chart.add('Opera', [.1, 1.6, .1, .5])
multipie_chart.render_to_file('./svg/pie.svg') 
SVG(filename='./svg/pie.svg')

# 折線圖
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file('./svg/line.svg') 
SVG(filename='./svg/line.svg')

# 世界地圖
worldmap_chart = pygal.Worldmap()
worldmap_chart.title = 'TW v.s. CN'
worldmap_chart.add('In 2014', {
                    'cn': 1000,
                    'tw': 6,
})
worldmap_chart.render_to_file('./svg/world.svg') 
SVG(filename='./svg/world.svg')

# Funnel 圖
funnel_chart = pygal.Funnel()
funnel_chart.title = 'V8 benchmark results'
funnel_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
funnel_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
funnel_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
funnel_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
funnel_chart.render_to_file('./svg/funnel.svg') 
SVG(filename='./svg/funnel.svg')

# 資料探索 Data Exploration
# Predict survival on Titanic 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./svg/train.csv")
df.info()

# 處理遺失值
# Remove Ticket, Cabin
df = df.drop(['Ticket','Cabin'], axis=1)

clear_df = df.fillna('Missing')

# Remove NaN values
df = df.dropna() 

# 算出死亡數
fig = plt.figure() 

# barplot and Horizotal barplot
df.Survived.value_counts().plot(kind='bar', rot=0)
#df.Survived.value_counts().plot(kind='barh', rot=90)
#ax1.set_xlim(-1, 2)
plt.title("Distribution of Survival, (1 = Survived)") 

# 死亡與年紀分布
plt.scatter(df.Survived, df.Age)
plt.ylabel("Age")                      
plt.grid(b=True, which='major', axis='y')  
plt.title("Survial by Age,  (1 = Survived)")

indexer = df.Age.value_counts().argsort()

# 根據艙等分布
df.Pclass.value_counts().plot(kind="barh")
#df.Pclass.value_counts().plot(kind='bar',rot=0)
#ax3.set_ylim(-1, len(df.Pclass.value_counts()))
plt.title("Class Distribution")

# 年紀與艙等分布
df.Age[df.Pclass == 1].plot(kind='kde')    
df.Age[df.Pclass == 2].plot(kind='kde')
df.Age[df.Pclass == 3].plot(kind='kde')

plt.xlabel("Age")    
plt.title("Age Distribution within classes")
plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best') 

# 上船地點
df.Embarked.value_counts().plot(kind='bar')
ax5.set_xlim(-1, len(df.Embarked.value_counts()))
plt.title("Passengers per boarding location")

# 性別與生存分析
fig = plt.figure(figsize=(18,6))
df.Survived[df.Sex == 'male'].value_counts().plot(kind='barh',label='Male')
df.Survived[df.Sex == 'female'].value_counts().plot(kind='barh', color='#FA2379',label='Female')
plt.title("Who Survived? with respect to Gender, (raw value counts) "); plt.legend(loc='best')

# 依比例來看
fig = plt.figure(figsize=(18,6))
(df.Survived[df.Sex == 'male'].value_counts()/float(df.Sex[df.Sex == 'male'].size)).plot(kind='barh',label='Male')  
(df.Survived[df.Sex == 'female'].value_counts()/float(df.Sex[df.Sex == 'female'].size)).plot(kind='barh', color='#FA2379',label='Female')
plt.title("Who Survived proportionally? with respect to Gender"); plt.legend(loc='best')


