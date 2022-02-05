from numpy import array
from matplotlib.pyplot import *

color_2 = array([63,81,181])/256
color_1 = array([199,0,57])/256
color_3 = array([63,185,83])/256

fig, ax = subplots(figsize=(4,4),frameon=False,facecolor="None")
for axis in ['top','bottom','left','right']:
	ax.spines[axis].set_linewidth(0)
ax.axis('off')
for item in [fig, ax]:
	item.patch.set_visible(False)

ax.add_artist(Circle((0.5,0.5),0.45,color=color_3,linewidth=8))
ax.add_artist(Rectangle((0.2,0.2),0.6,0.6,color=color_1,linewidth=3,fill=False))
ax.add_artist(Rectangle((0.2,0.2),0.6,0.2,color=color_2,linewidth=8,fill=False))
ax.add_artist(Rectangle((0.2,0.2),0.2,0.2,color=color_2,linewidth=8,fill=False))
ax.add_artist(Rectangle((0.2,0.2),0.2,0.6,color=color_2,linewidth=8,fill=False))

text(0.6,0.58,"M",rotation=0,fontsize=60,ha="center",va="center",color=color_1,fontweight="bold")
text(0.3,0.58,"1",rotation=0,fontsize=30,ha="center",va="center",color=color_1,fontweight="bold")
text(0.3,0.28,"0",rotation=0,fontsize=30,ha="center",va="center",color=color_1,fontweight="bold")
text(0.6,0.28,"x",rotation=0,fontsize=40,ha="center",va="center",color=color_1,fontweight="bold")
xlabel(" ");		xticks([]);			xlim([0,1])
ylabel(" ");		yticks([]);			ylim([0,1])
tick_params(top=False,right=False,left=False,bottom=False)
subplots_adjust(left=0,right=1, top=1, bottom=0.0) 
savefig("math101.svg", dpi=300)
show()