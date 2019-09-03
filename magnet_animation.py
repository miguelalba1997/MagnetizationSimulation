import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams
N = 100
magnet = np.zeros((N, N))
#create four lists of nieghbors that will influence
#the current atoms magnetization.
ja = [[0]*N for y in range(N)]
jb = [[0]*N for y in range(N)]
jc = [[0]*N for y in range(N)]
jd = [[0]*N for y in range(N)]
je = [[0]*N for y in range(N)]
jf = [[0]*N for y in range(N)]
jg = [[0]*N for y in range(N)]
jh = [[0]*N for y in range(N)]

J = 1.0 
width = .7 #determines the disorder of the system
t = 1.6 #temperature
mix = .35 

for x in range(N):
    for y in range(N):
        ja[x][y] = J + width*random.uniform(-1,1)
        jb[x][y] = J + width*random.uniform(-1,1)
        jc[x][y] = J + width*random.uniform(-1,1)
        jd[x][y] = J + width*random.uniform(-1,1)
        je[x][y] = J + width*random.uniform(-1,1)
        jf[x][y] = J + width*random.uniform(-1,1)
        jg[x][y] = J + width*random.uniform(-1,1)
        jh[x][y] = J + width*random.uniform(-1,1)
        magnet[x,y] = random.uniform(-1,1)
def mag(data):
    global magnet
    new_mag = magnet.copy()
    for x in range(N):
        for y in range(N):
            a = magnet[x, (y-1)%N]
            b = magnet[x, (y-1)%N]
            c = magnet[(x-1)%N, y]
            d = magnet[(x+1)%N, y]
            e = magnet[(x-1)%N, (y-1)%N]
            f = magnet[(x+1)%N, (y-1)%N]
            g = magnet[(x-1)%N, (y-1)%N]
            h = magnet[(x+1)%N, (y+1)%N]

            field = (a*ja[x][y] + b*jb[x][y] + c*jc[x][y] + d*jd[x][y]+
                    e*je[x][y] + f*jf[x][y] + g*jg[x][y] + h*jh[x][y])/t
            new_mag[x][y] = mix*math.tanh(field) + (1.0 - mix)*magnet[x][y]
    mat.set_data(new_mag)
    magnet = new_mag
    return [mat]
# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(magnet, cmap = 'hot')
ani = animation.FuncAnimation(fig, mag, interval=200,
                              save_count=100)
ani.save('magnet.gif', writer='imagemagick', fps=10)



