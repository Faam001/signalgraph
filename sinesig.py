#Dicek dulu apabila venv sudah aktif untuk memakai lib 
#gunakan source ../sig/bin/activate

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

print("input the signal's ω")
O = int(input('enter here:  '))
x = np.arange(0, O*np.pi, 0.01)
print('input the amplitude')
A = int(input('enter here:  '))
y = A * np.sin(x)

fig = plt.figure()
ax = plt.subplot(1, 1, 1)

print('how many data skip?')
data_skip = int(input('enter here:  '))

def init_func():
    ax.clear()
    plt.xlabel('t')
    plt.ylabel('f(t)')


def update_plot(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
    ax.scatter(x[i], y[i], marker='o', color='r')
    plt.xlim(((x[0], x[-1])))
    plt.ylim((-A, A))

anim = FuncAnimation(fig, update_plot, frames=np.arange(0, len(x), data_skip), interval=20)

#save as gif memakai imagemagick
anim.save('sinesig.gif' , dpi=150, fps=30, writer='imagemagick')

print('saved')