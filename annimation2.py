import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.io import loadmat


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

im = plt.imshow(h_mnt,extent = [125000,225000,125000,225000], animated=True)
ax = plt.gca()
line, = ax.plot([], [],'r') 
line1, = ax.plot([], [],'g') 

def updatefig(i):
    im.set_array(h_mnt)
    line.set_data(particules[i,:,0],particules[i,:,1])
    line1.set_data(trajectoire[:i,0],trajectoire[:i,1])
    return im,line,line1

ani = animation.FuncAnimation(fig, updatefig, frames = 720,interval=50, blit=True)
# ani.save('filtre_particulaire.gif',writer= 'imagemagik',fps = 10)
plt.show()