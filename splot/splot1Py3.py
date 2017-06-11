import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import itertools
from pylab import rcParams
#rcParams['figure.figsize'] = 12, 8    #### Figure reshape Method 1: but the aspect ratio also depends on the data. I don't know if this gonna work for general plot
plt.style.use('../splot/styles/billinge.mplstyle')
#plt.style.use('../splot/styles/mycopy.mplstyle')
c = [color['color'] for color in list(rcParams['axes.prop_cycle'])]

def data(data, samplename='none', scan='scan', line = None, color = None, marker = None):
    d = {}
    d['samplename'] = samplename
    d['scanname'] = samplename + scan
    d['data'] = data
    if line:
        d['line'] = line
    if color:
        d['color'] = color
    if marker:
        d['marker'] = marker
    return d

class Splot:
    def __init__(self, r = 1, c = 1):
        self.row, self.col = r, c
        self.fig, self.ax = plt.subplots(self.row,  self.col, sharex='col', sharey='row',)
                            #figsize = (8, 6)) #### Figure reshape Method 2: Similar to Method 1, but can be specific for each plot. Cons: Use has to come to here to change the code....
        self.fig.tight_layout()
        self.axBig = self.fig.add_subplot(111, frameon = False)
        self.axBig.tick_params(labelcolor ='none', top ='off', bottom ='off', left ='off', right ='off')
        self.axBig.grid(False)
        self.legends = ([], [])
        self.subD = np.empty( (self.row,  self.col), object)
        for i, j in itertools.product(range(r), range(c)):
            self.subD[i,j] = ([], [])
        self.fig.subplots_adjust(wspace = 0.0, hspace = 0.0)
        if r == 1 and c == 1:
            self.ax = np.array([self.ax]).reshape(-1, 1)
        elif r == 1 or c == 1:
            self.ax = self.ax.reshape((r, c))

    def plotData(self, d, r = 0, c = 0, scal = 1, offsetx = 0, offsety = 0, diff = False, legend = None):
        line, = self.ax[r, c].plot( d['data'][0] + offsetx, d['data'][1]*scal + offsety, \
                                label = d['scanname'])
        if 'line' in d:
            plt.setp(line, linestyle = d['line'])
        if 'color' in d:
            plt.setp(line, color = d['color'])
        if 'marker' in d:
            plt.setp(line, marker = d['marker'])
        self.addData(d, r, c)
        if d['scanname'] not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append(d['scanname'])
        if diff == True:
            self.diffC(r, c)
        self.ticks()
        self.label()
        self.title()
        self.legend(disp = legend)

    def addData(self, d, r, c):
        self.subD[r, c][0].append( d['data'][0] )
        self.subD[r, c][1].append( d['data'][1] )
        return self.subD

    def diffC(self, r=0, c=0, scal=1, offset = None):
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
        if offset == None:
            h = max (self.subD[r, c][1][0].max(), self.subD[r, c][1][1].max())
            l = min (self.subD[r, c][1][0].min(), self.subD[r, c][1][1].min() )
            amp = h-l
            offset = l - diffy.max() - amp*0.1
        line, = self.ax[r, c].plot( self.subD[r,c][0][0], diffy*scal + offset, \
                label = 'diff')
        plt.setp(line, color = 'g')
        plt.setp(line, linestyle = '-')
        if "diff" not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append('diff')

    def ticks(self):
#        nbins = len( self.ax[0, 0].get_xticklabels() )
        nbins = 6                   #??? fix a grid density
        for i in range(self.row):
            self.ax[i, 0].yaxis.set_major_locator(MaxNLocator(nbins, prune='both'))
            self.ax[i, 0].minorticks_on()
        for i in range(self.col):
            self.ax[-1, i].xaxis.set_major_locator(MaxNLocator(nbins, prune='both'))
            self.ax[-1, i].minorticks_on()

    def label(self, x = 'r', xunit = 'AA', y = 'G', yunit = 'AA^{-2}', math = 'on'):
        if math == 'on':
            xl = r'$\mathrm{%s}\  \mathrm{( \%s )}$' %(x, xunit)
            yl = r'$\mathrm{%s}\  \mathrm{( \%s )}$' %(y, yunit)
        if math == 'off':
            xl = '%s (%s)' %(x, xunit)
            yl = '%s (%s)' %(y, yunit)
        self.axBig.set_xlabel(xl)
        self.axBig.set_ylabel(yl)

    def title(self, t = '', math = 'off'):
        if math == 'on':
            t = r'$\mathrm{%s} $' %t
        self.axBig.set_title(t)

    def legend(self, disp = None):
        if disp:
            if disp == 'out':
                self.legendOut()
            if disp == 'in':
                self.legendIn()
    def legendOut(self):
        plt.legend(self.legends[0], self.legends[1], \
            loc='center left', bbox_to_anchor = (1, 0.6), borderaxespad=0, \
            labelspacing= 1., prop={'size':8}, handlelength = 3)
    def legendIn(self):
        for i, j in itertools.product(range(self.row), range(self.col)):
            self.ax[i,j].legend(
                                loc = 'upper right', \
                                labelspacing= 1., prop={'size':8}, handlelength = 3)

    def save(self, name = "myplot", form = "pdf"):
        return self.fig.savefig(name+"."+form)

    def show(self):
        return self.fig.show()

    def figureSize(self, width, height): #### Figure reshape Method 3: Similar to Method 1 or 2. This changes the overal figure shape. Recommend to use this one :)
        self.fig.set_figwidth(width)
        self.fig.set_figheight(height)

    def aspect(self, ratio): #### Figure reshape Method 4: rescale subplot axes box. Doesn't work well, not recommend....
        for i, j in itertools.product(range(self.row), range(self.col)):
            ll, ur = self.ax[i,j].get_position() * self.fig.get_size_inches()
            width, height = ur - ll
            axes_ratio = height / width
            aspect = axes_ratio / self.ax[i,j].get_data_ratio()
#            self.ax[i, j].set_aspect (ratio * aspect, adjustable='box-forced') # Cons: may sepearte the subplots
            self.ax[i, j].set_aspect (ratio * aspect) # Cons: may cut off part of the data

