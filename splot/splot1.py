#!/Users/Shuyue/mc/envs/py27/bin/python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('styles/mycopy.mplstyle')

class Splot:   
    global groupColor, d1, d2, d
    groupColor = [color['color'] for color in list(plt.rcParams['axes.prop_cycle'])]
    
#    d is the default use, if you don't have random data to visulize, 
#    you can always load them to the d 
    d = {'Name': '', 'Data': ([], []), 'Color': groupColor[0], 'marker': ' ',
    'line': '-'}
    d1 = {'Name': 'Ni', 'Data': ([], []), 'Color': groupColor[6],
    'marker': '+' , 'line': ''}
    d2 = {'Name': 'Zn', 'Data': ([], []), 'Color': groupColor[4], 'marker': '^',
    'line': '--'}
        
    def __init__(self, r = 1, c = 1):
        self.row, self.col = r, c
        self.data = np.zeros( (self.row, self.col), object)
        self.fig, self.ax = plt.subplots(self.row,  self.col, \
                            sharex='col', sharey='row')
        self.fig.subplots_adjust(wspace = 0.0, hspace = 0.0)
        if r == 1 and c == 1:
            self.ax = np.array([self.ax]).reshape(-1,1)    
        elif r == 1:
            self.ax = self.ax.reshape((1, c))
        elif c == 1:
            self.ax = self.ax.reshape((r, 1))
         
    def plotData(self, dat = d, x=1, y=1):
#        self.addData(dat['Data'][0], dat['Data'][1], x, y)
        Subplot(self.ax[x-1, y-1], dat)
    def addData(self, r, q, x, y): 
        self.data[x-1, y-1] = (r, q)
        return self.data
        
    #Another method to change the plot ratio
    def ratio(self, (r1, c1), (r2, c2)):
        pass

# +++++++++++++++++++++++++++++++ Subplot Class +++++++++++++++++++++++++++++++ 
class Subplot:
    def __init__(self, axes, dat = d):
        self.ax = axes
        line = self.ax.plot(dat['Data'][0], dat['Data'][1], marker = dat['marker'])
        plt.setp(line, color = dat['Color']) 
        plt.setp(line, linestyle = dat['line'])    
        
    def scale(self, sx = 1, sy = 1): #scale the data by a fator of s
        newDat = (self.dat['Data'][0]*sx, self.dat['Data'][1]*sy)
        return newDat
    
    def offSet(self, ox = 0, oy = 0): 
        newDat = (self.dat['Data'][0] + ox, self.dat['Data'][1] + oy)
        return newDat

