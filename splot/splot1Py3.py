import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 
import itertools
#plt.style.use('../splot/styles/mycopy.mplstyle')
plt.style.use('../splot/styles/billinge.mplstyle')
c = [color['color'] for color in list(plt.rcParams['axes.prop_cycle'])]
        
def Data(data, samplename='none', scan='scan', color= c[0], marker='+', line='-'):
    d = {}
    d['samplename'] = samplename
    d['scanname'] = samplename+scan
    d['data'] = data
    d['color'] = color
    d['marker'] = marker
    d['line'] = line
    return d
    
class Splot: 
    def __init__(self, r = 1, c = 1):
        self.row, self.col = r, c
        self.fig, self.ax = plt.subplots(self.row,  self.col, sharex='col', sharey='row')
        self.axBig = self.fig.add_subplot(111, frameon=False) 
        plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
        self.axBig.grid(False)        
        self.legends = ([], [])        
        self.subD = np.empty( (self.row,  self.col), object)        
        for i, j in itertools.product(range(r), range(c)):
            self.subD[i,j] = ([], [])
        self.fig.subplots_adjust(wspace = 0.0, hspace = 0.0)
        if r == 1 and c == 1:
            self.ax = np.array([self.ax]).reshape(-1,1)    
        elif r == 1:
            self.ax = self.ax.reshape((1, c))
        elif c == 1:
            self.ax = self.ax.reshape((r, 1))
        
    def plotData(self, d, r = 0, c = 0, scal=1, offset=0, diff = False):
        line, = self.ax[r, c].plot( d['data'][0], d['data'][1]*scal + offset, \
                                   marker = d['marker'], label = d['scanname'])
        plt.setp(line, color = d['color'])
        plt.setp(line, linestyle = d['line'])
        self.addData(d, r, c)        
        if d['scanname'] not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append(d['scanname'])
        if diff == True:
            self.diffC(r, c, offset = d['data'][1].min()-5) # Plot the diff 5 units below 
        self.ticks()
        self.label()        
        self.title()
        self.legendOut()
        self.fig.subplots_adjust(bottom = 0.2, right = 0.85) #room for the xlable and legend
        
    def addData(self, d, r, c):
        self.subD[r, c][0].append( d['data'][0] )
        self.subD[r, c][1].append( d['data'][1] )   
        return self.subD
    
    def diffC(self, r=0, c=0, scal=1, offset=0): #Not sure if you want to scale / offset this curve
        if len (self.subD[r, c][1]) == 0:
            print ("subplot", (r,c), "hasn't been load with any data")
            return
        elif len (self.subD[r, c][1]) == 1:
            print ("subplot", (r,c), "needs one more curve to compute the diff Curve")
            diffy = self.subD[r, c][1][0] - self.subD[r, c][1][0]
        elif len (self.subD[r, c][1]) > 2:
            print ("subplot", (r,c), "has more than 2 curves, i'm confused now...")
            return
        else:
            diffy = self.subD[r,c][1][0] - self.subD[r, c][1][1]
        line, = self.ax[r, c].plot( self.subD[r,c][0][0], diffy*scal + offset, \
                label = 'diff')
        plt.setp(line, color = 'g')
        plt.setp(line, linestyle = '-')
        if "diff" not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append('diff')
        self.legendOut()
        
    def ticks(self): 
#        nbins = len( self.ax[0, 0].get_xticklabels() )
        nbins = 4                   #??? fix a grid density
        for i in range(self.row):
            self.ax[i, 0].yaxis.set_major_locator(MaxNLocator(nbins, prune='both')) 
            self.ax[i, 0].minorticks_on()
        for i in range(self.col):
            self.ax[-1, i].xaxis.set_major_locator(MaxNLocator(nbins, prune='both')) 
            self.ax[-1, i].minorticks_on()

    def label(self, x = 'r', xunit = 'AA', y = 'G', yunit = 'AA^{-2}', math = 'on'): 
        if math == 'on':
            xl = r'$'+ x +'$ '+ '$(\mathrm{\\' + xunit + '})$'
            yl = r'$'+ y +'$ '+ '$(\mathrm{\\' + yunit + '})$'
        if math == 'off':
            xl = " "+ x +' ('+ xunit +')'
            yl = " "+ y +' ('+ yunit +')'
        self.axBig.set_xlabel(xl)
        self.axBig.set_ylabel(yl)
    
    def title(self, t = '', math = 'on'):
        if math == 'on':
            t = r'$'+ t +'$'
        self.axBig.set_title(t)
    
    def legendOut(self):    #??? where to place the legend on the plot?
        plt.legend(self.legends[0], self.legends[1], \
            loc='center left', bbox_to_anchor = (1, 0.85), borderaxespad=0, \
            labelspacing= 1., prop={'size':8})
    
    def save(self, name = "myplot", form = "pdf"):
        return self.fig.savefig(name+"."+form)