from ThreeShots import ThreeShots
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

shots = ThreeShots.FromDir(None, 'Foscam\\Day_Cat_nomotionsnap')
shots.delta12.DrawContours(shots.shot2)
shots.delta31.DrawContours(shots.shot2)
shots.delta23.DrawContours(shots.shot3)
shots.delta12.DrawContours(shots.shot3)
shots.delta31.DrawContours(shots.shot1)
shots.delta12.DrawContours(shots.shot1)

plt.figure(figsize=(12, 6.025))
gs1 = gridspec.GridSpec(2, 3, left=0, right=1, top=1,
                        bottom=0, wspace=0, hspace=0)
# gs2 = gridspec.GridSpec(1, 2, left=0, right=1, top=1,
#                         bottom=0, wspace=0, hspace=0)
# gs1.update() # set the spacing between axes.

plt.subplot(gs1[2])
shots.shot1.show_plt()
plt.subplot(gs1[5])
shots.shot3.show_plt()

plt.subplot(gs1[:2,:2]) # 
shots.shot2.show_plt()

plt.tight_layout()
plt.margins(0)
# plt.figure.canvas.toolbar.pack_forget()
plt.show()
#plt.savefig(filename, transparent = True, bbox_inches = 'tight', pad_inches = 0)
