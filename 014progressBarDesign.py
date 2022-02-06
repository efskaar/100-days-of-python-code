# -*- coding: utf-8 -*-
from numpy import *
from matplotlib.pyplot import *

parts = 4
grayScale = 32
uioColors = [226/255,4/255,19/255]
backgroundColor = [grayScale/255,grayScale/255,grayScale/255]; 
x = linspace(0,parts-1,parts)
y = 0.5
m = 0.6
xSize = 20
ySize = 1
resolution = 1080
dpi = resolution/xSize
set_linewidth = 5
for x_ in x:
	fig, ax = subplots(figsize=(xSize,ySize),frameon=False,facecolor="None")
	for axis in ['top','bottom','left','right']:
		ax.spines[axis].set_linewidth(0)
	ax.axis('off')
	for item in [fig, ax]:
		item.patch.set_visible(False)
	plot([x_/2,0,parts-1,x_/2],[y,y,y,y],"-",color=backgroundColor,linewidth=set_linewidth)
	plot([x_/2,0,x_,x_/2],[y,y,y,y],"-",color=uioColors,linewidth=set_linewidth)
	xlabel(" ")
	ylabel(" ")
	xticks([])
	yticks([])
	xlim([0,parts-1])
	ylim([0.45,0.55])
	tick_params(top=False,right=False,left=False,bottom=False)
	subplots_adjust(left=0,right=1, top=1, bottom=0.0) 
	#savefig("progress-bar%d%d.png" % (x_+1,set_linewidth), dpi=dpi)
	show()



