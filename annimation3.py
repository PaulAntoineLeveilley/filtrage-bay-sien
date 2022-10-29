import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io import loadmat
from mpl_toolkits import mplot3d
from matplotlib import cm


with open('TP4/particules.npy','rb') as f:
    particules = np.load(f)
with open('TP4/trajectoire.npy','rb') as f:
    trajectoire = np.load(f)

data = loadmat('TP4/carte_centreMetres.mat');

h_mnt = data["h_MNT"]
h_mnt = np.flip(h_mnt,axis = 0)
x_mnt = data["x_MNT"]
y_mnt = data["y_MNT"]

fig = plt.figure()
plt.title('Trajectoire et estimation par filtrage particulaire au cours du temps')

# y_mnt_1 = np.flip(y_mnt[0])

indice_y_min=350
indice_y_max=550
indice_x_min=400
indice_x_max=600

x_red = x_mnt[:,indice_x_min:indice_x_max]
y_red = y_mnt[:,indice_y_min:indice_y_max]
h_red = h_mnt[indice_y_min:indice_y_max,indice_x_min:indice_x_max]

ax = plt.axes(projection='3d')

x,y = np.meshgrid(x_red,y_red)
mappable = plt.cm.ScalarMappable()
mappable.set_array(h_red)

ax.plot_surface(x, y, h_red, cmap=mappable.cmap, norm=mappable.norm, linewidth=0, antialiased=False)
graph, = ax.plot(particules[0,:,0],particules[0,:,1],particules[0,:,2], linestyle="", marker="o",c='r',markersize='1')
graph2, = ax.plot(trajectoire[:0,0],trajectoire[:0,1],trajectoire[:0,2],'g',linestyle="-")
plt.title('Navigation par corrélation de terrain')
plt.legend(['estimation par filtrage particulaire','trajectoire réelle'])
def updatefig(i):
    graph.set_data (particules[i,:,0],particules[i,:,1])
    graph.set_3d_properties(particules[i,:,2])
    graph2.set_data (trajectoire[:i,0],trajectoire[:i,1])
    graph2.set_3d_properties(trajectoire[:i,2])
    # line2.set_data(trajectoire[:i,0],trajectoire[:i,1],trajectoire[:i,2])
    return graph,graph2

ani = animation.FuncAnimation(fig, updatefig, frames = 720,interval=50, blit=True)
# ani.save('filtre_particulaire.gif',writer= 'imagemagik',fps = 10)
plt.show()
