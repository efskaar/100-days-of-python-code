from numpy import *
from matplotlib.pyplot import *

fig, ax = subplots(figsize=(10,10),frameon=False,facecolor="None")
for axis in ['top','bottom','left','right']:
	ax.spines[axis].set_linewidth(0)
ax.axis('off')
for item in [fig, ax]:
	item.patch.set_visible(False)

#eye
ax.add_artist(Circle((0.5,0.5),0.435,color=[0.5,0.5,0.5],linewidth=5,fill=False))
ax.add_artist(Circle((0.5,0.5),0.430,color=[0,0,0],linewidth=15,fill=False))
ax.add_artist(Circle((0.5,0.5),0.42,color=[0.5,0.5,0.5],linewidth=3))
ax.add_artist(Circle((0.5,0.5),0.2,color=[0.05,0.05,0.05],linewidth=3))
text(0.50,0.775,"HOW",rotation=0,fontsize=100,ha="center",va="center",color="white")
text(0.5,0.20,"SEE IT",rotation=0,fontsize=100,ha="center",va="center",color="white")

xlabel(" ");		xticks([]);			xlim([0,1])
ylabel(" ");		yticks([]);			ylim([0,1])

tick_params(top=False,right=False,left=False,bottom=False)
subplots_adjust(left=0,right=1, top=1, bottom=0.0) 
savefig("hisi.svg", dpi=300)
show()