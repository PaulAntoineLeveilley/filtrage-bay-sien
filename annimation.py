import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('TP2/dyn.npy','rb') as f:
    dynamique = np.load(f)
with open('TP2/kalman.npy','rb') as f:
    kalman = np.load(f)
with open('TP2/cov.npy','rb') as f:
    cov = np.load(f)

dt = 0.01

fig = plt.figure(figsize=(6, 3))
ax1 = plt.subplot2grid(shape=(2, 2), loc=(0, 0), rowspan=2)
ax2 = plt.subplot2grid(shape=(2,2), loc=(0, 1), colspan=1)
ax3 = plt.subplot2grid(shape=(2,2), loc=(1, 1), colspan=1)


 # initialise la figure
line, = ax1.plot([], []) 
line2, = ax1.plot([], []) 
line3, = ax2.plot([], []) 
line4, = ax2.plot([], [])

line5, = ax3.plot([], []) 
line6, = ax3.plot([], [])

line7, = ax2.plot([], [])
line8, = ax3.plot([], [])

ax1.set_title("Trajectoire du mobile et estimation")
ax1.legend(["trajectoire réelle","estimation par filtre de Kalman"])
ax1.set_xlim(np.min(dynamique[:,0]-100), np.max(dynamique[:,0])+100)
ax1.set_ylim(np.min(dynamique[:,1])-100, np.max(dynamique[:,1])+100)

n,_ = np.shape(dynamique)
variance_x = cov[:,0,0]
intervalle_conf_x_sup = kalman[:,0]+2*variance_x
intervalle_conf_x_inf = kalman[:,0]-2*variance_x
variance_y = cov[:,1,1]
intervalle_conf_y_sup = kalman[:,1]+2*variance_y
intervalle_conf_y_inf = kalman[:,1]-2*variance_y

ax2.set_ylim(-12000,0)
ax2.set_xlim(0,1)
ax2.set_title("x et intervalle de confiance à 95%")


ax3.set_ylim(3000,10000)
ax3.set_xlim(0,1)
ax3.set_title("y et intervalle de confiance à 95%")

def animate(i): 
    t = i 
    line.set_data(dynamique[0:t,0], dynamique[0:t,1])
    line2.set_data(kalman[0:t,0],kalman[0:t,1])
    T = np.linspace(0,1,n)
    line3.set_data(T[:t],intervalle_conf_x_sup[:t])
    line4.set_data(T[:t],intervalle_conf_x_inf[:t])

    line5.set_data(T[:t],intervalle_conf_y_sup[:t])
    line6.set_data(T[:t],intervalle_conf_y_inf[:t])
    
    line7.set_data(T[:t],kalman[:t,0])
    line8.set_data(T[:t],kalman[:t,1])

    return line, line2, line3,line4,line5, line6,line7,line8
 
ani = animation.FuncAnimation(fig, animate, frames=n,
                              interval=1, blit=True, repeat=False)
plt.show()