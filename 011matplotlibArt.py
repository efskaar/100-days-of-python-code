# -*- coding: utf-8 -*-
from matplotlib.pyplot import * 
from random import random
import matplotlib

dpi = 55
matplotlib.use("svg") #Agg for png, svg for svg
filetype = "svg"
fig, ax = subplots(figsize=(9,9),frameon=False,facecolor=(0,0,0))
ax.axis('off')
for axis in ['top','bottom','left','right']:
	ax.spines[axis].set_linewidth(0)
for item in [fig, ax]:
	item.patch.set_visible(False)
tick_params(top=False,right=False,left=False,bottom=False)

plot([0,100,100,0,0],[0,0,100,100,0],'r-',linewidth=3)
for x in range(1,100,2):
  for y in range(1,100,2):
    plot(x,y,'o',color=[random(),random(),random()])

xlim([0,100])
ylim([0,100])
subplots_adjust(left=0,right=1, top=1, bottom=0.0) 
savefig(f'art-{dpi:d}-.{filetype}', dpi=dpi)