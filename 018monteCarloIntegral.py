from matplotlib.pyplot import *
from random import * 
from numpy import *
import matplotlib
import os

dpi = 120
filetype = 'png'
folder = "monte-carlo-%s-%d" % (filetype,dpi)
try:
	os.mkdir(folder)
except:
	None
maks = 30
red = 226/255
green = 4/255
blue = 19/255
f1 = [red,green,blue]
f2 = [blue,red,green]
f3 = [red/1.5,red/1.5,red/1.5]

def func(x):
	return 20+5*sin(x/10)+x/5

fig, ax = subplots(figsize=(9,9),frameon=False,facecolor=(0,0,0))
for axis in ['top','bottom','left','right']:
	ax.spines[axis].set_linewidth(0)
ax.axis('off')

for item in [fig, ax]:
	item.patch.set_visible(False)
tick_params(top=False,right=False,left=False,bottom=False)
xlim([-20,100])
ylim([0,100])

plot([-20,100],[0,0],linewidth=16,color=f3)
plot([0,0],[0,100],linewidth=8,color=f3)

val = linspace(1,100,1000)
plot(val,func(val),linewidth=8,color=f3)

sick = 0
healthy = 0
i = 0
x = 100*random.rand(1010)
y = 100*random.rand(1010)

for x_,y_ in zip(x,y):
	if y_ > func(x_):
		scatter(x_,y_,s=100,color=f1)
		sick += 1
	else:
		scatter(x_,y_,s=100,color=f2)
		healthy += 1
	summen = healthy+sick
	height_healthy = 100*healthy/summen
	height_sick = 100*sick/summen
	if i%1 == 0:
		bar(-10,100,width=8,color=f1)
		bar(-10,height_healthy,width=8,color=f2)
		count = (4-len(str(int(i))))*"0"+ str(int(i))
		savefig(f"{folder}/progress-bar{count}.{filetype}", dpi=dpi)
	i += 1
	print(i)