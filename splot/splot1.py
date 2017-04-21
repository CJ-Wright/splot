#!/Users/Shuyue/mc/envs/py27/bin/python
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('styles/mycopy.mplstyle')
c = [color['color'] for color in list(plt.rcParams['axes.prop_cycle'])]

class Data:
    def __init__(self, data, samplename='none',scan='scan',
                 color= c[0], marker='+', line=''):
        self.samplename = 'samplename'
        self.scanname = self.samplename+'scan'
        self.data = data
        self.color = color
        self.marker = marker
        self.line = line
    
class Splot:   
    def __init__(self, r = 1, c = 1):
        self.row, self.col = r, c
        self.fig, self.ax = plt.subplots(self.row,  self.col, sharex='col', sharey='row')
        self.fig.subplots_adjust(wspace = 0.0, hspace = 0.0)
        if r == 1 and c == 1:
            self.ax = np.array([self.ax]).reshape(-1,1)    
        elif r == 1:
            self.ax = self.ax.reshape((1, c))
        elif c == 1:
            self.ax = self.ax.reshape((r, 1))
         
    def plotData(self, d, r = 1, c = 1, scal=1, offset=0, diff = False):
        line = self.ax[r-1, c-1].plot( d.data[0], d.data[1]*scal + offset, \
                                       marker = d.marker)
        plt.setp(line, color = d.color) 
        plt.setp(line, linestyle = d.line)
        
#================================== Test ======================================
x = np.linspace(-4, 4, 80)
y = x**3

x2 = np.linspace(-6, 6, 80)
y2 = x2**2

# data setup
d300 = Data( (x, y), samplename ='Ni', scan = '300K', color = c[6])
d500 = Data( (x2, y2), 'Ni', '500K')

# plot axis setup
H = Splot(3, 1)
#H.1.1.diff = T

# plot data setup
H.plotData(d300, 1, 1)
H.plotData(d500, 1, 1, scal = 0.5, offset = 0.2, diff = True)
H.plotData(d300, 2, 1, scal = 0.6)
plt.show()