import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

# Upload table
df = pd.read_csv("Rookie season stats.csv")

# Add 2 more columns
df['Total_PTS'] = df['PTS'] * df['G']
df['Points_Per_Minute'] = df['Total_PTS'] % df['MP']

# Minimize db

sf = df[['Total_PTS','Player','Points_Per_Minute']]

# Upload images

luka = mpimg.imread('d.png')
james = mpimg.imread('james.png')
jordan = mpimg.imread('jordan.png')
kobe = mpimg.imread('kobe.png')
harden = mpimg.imread('harden.png')
curry = mpimg.imread('curry.png')
k_d = mpimg.imread('kd.png')
pic = [luka, james, jordan, kobe, harden, curry, k_d]
# Setting the graph

fig, ax = plt.subplots(figsize=(15, 8))
ax.clear()
x_pos= np.arange(1,8)
width = 0.4
ax.set_xlim(0, 8)
ax.set_ylim(0, 3000)
plt.bar(x_pos,sf.Points_Per_Minute*30,width = 0.4 , label = 'Points_Per_Minute * 30')
plt.bar(x_pos+width,sf.Total_PTS,width = 0.4 , label = 'Total_PTS')
plt.xticks(x_pos+width/2,sf.Player)

# Add the points text on the charts

for i in enumerate(sf['Total_PTS']):
    ax.text(i[0]+1.25, i[1]-100, int(i[1]),size=12, weight=600,)
for i in enumerate(sf['Points_Per_Minute']):
    ax.text(i[0]+0.85, i[1]*20,int(i[1]),size=14, weight=600, )

# resize images

kdbox = OffsetImage(luka, zoom=0.5)
kdbox1 = OffsetImage(james, zoom=0.5)
kdbox2 = OffsetImage(jordan, zoom=0.5)
kdbox3 = OffsetImage(kobe, zoom=0.5)
kdbox4 = OffsetImage(k_d, zoom=0.5)
kdbox5 = OffsetImage(harden, zoom=0.5)
kdbox6 = OffsetImage(curry, zoom=0.5)

# Position the images

a1 = AnnotationBbox(kdbox, (1.2, 1900),frameon= False)
a2 = AnnotationBbox(kdbox1, (2.2, 2100),frameon=False)
a3 = AnnotationBbox(kdbox2, (3.2, 2650),frameon=False)
a4 = AnnotationBbox(kdbox3, (4.2, 1000),frameon=False)
a5 = AnnotationBbox(kdbox4, (5.2, 2100),frameon=False)
a6 = AnnotationBbox(kdbox5, (6.2, 1200),frameon=False)
a7 = AnnotationBbox(kdbox6, (7.2, 1900),frameon=False)

# Add images to graph

ls =[a1, a2, a3, a4, a5, a6, a7]
for i in ls:
    ax.add_artist(i)
plt.draw()

# Add title, legend and y label

plt.title('Rookie season stats',transform=ax.transAxes, size=24, weight=600, )
plt.legend(loc='best')
plt.ylabel('points', size=16, weight=400)
plt.show()
