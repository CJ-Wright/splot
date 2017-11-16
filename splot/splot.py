##############################################################################
#
# simonplot(splot)       by Billinge Group
#                        Simon J. L. Billinge sb2896@columbia.edu
#                        (c) 2017 trustees of Columbia University in the City of
#                            New York.
#                        All rights reserved
#
# File coded by:    Shuyue Xue
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
###############################################################################
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import itertools
plt.style.use('../splot/styles/manuscripture.mplstyle')
bgcolor = [color['color'] for color in list(plt.rcParams['axes.prop_cycle'])]   

def data_dict(dataPath, samplename='', scan='', **kwargs):
    """Make a data dictionary with keys: data, samplename, scanname,
    and optional keys to specify plotting style: line, color, and marker.

    Parameters:
    -------------
    dataPath:str
        the data file path 
    samplename: str
        sample name
    scan: str
        scan name
    **kwargs: dict
        kwargs for plotting the Meas line style passed to plt.plot

    Returns: dict
    --------
        A dictionary with keys: 'Meas', (may have 'Calc' and 'Diff' depending 
        on the data file), 'samplename', 'scanname', and kwargs for the Meas.
        'meas' -- Measured g(r)
        'Calc' -- Calculated g(r)
        'Diff' -- Calculted difference between Measured and Calculated g(r).
    """
    from splot.loaddata import loadData
    d = {}
    d['samplename'] = samplename
    d['scanname'] = samplename + scan
    arr = loadData(dataPath, unpack=True)
    if len(arr) == 2:
        r, meas = arr
    if len(arr) == 4:
        r, meas, diff, calc = arr
        d['Calc'] = (r, calc)
        d['Diff'] = (r, diff)
    d['Meas'] = (r, meas)    
    d.update(kwargs)
    return d

class Splot:
    """Contains functions for quick plotting Billinge Group Standard figures.

    User must generate a data dictionary by the data function in this module.
    This class only handles plotting.

    Attributes:
    -------------
    row: int
        the number of rows in the plotting panel. Default value is 1 row.
    col: int
        the number of columns in the plotting panel. Default value is 1 column.
    fig: object
        the figure object in matplotlib.
    ax: ndarray
        a 2D array of same number of rows and cols as in the plotting panel.
        Each entry contains a matplotlib axes to plot each subplot.
    axbig: oject
        a matplotlib axes to make tile and labels for overall plot.
    legends: tuple
        in the form of (lines, labels)
        where the lines is an array of line objects
        and the labels is an array of the scan names of the data that are used
        as the legends in the figure.
    datasets_styles: dict
        a dictionary containing plotting styles used on each data dictionary. 
        Once being plotted, the data dictionary sticks with the same style.
    subd: ndarry
        a 2D array of same number of rows and cols as in the plotting panel.
        Each entry is a dictionary of the data at the corresponding panel. 
        The keys are the scanname modified with data type (Meas, Calc, Diff), 
        or if scaled or offset during plotting. 
        The value is the data being plotted. 
    thiscolor: int
        color number from group colormap that is set to the line being plotted.
    colorcheck: list
        Billinge Group color map in rgb values. 
    whitelist: list
        a list of keys that does not exit in matplotlib but in data dictionary. 
    """

    def __init__(self, r=1, c=1):
        """Create a new plotting panel as r rows by c colums."""
        self.row, self.col = r, c
        if self.row > self.col:
            plt.rcParams["figure.figsize"] = (6, 8)
        if self.row < self.col:
            plt.rcParams["figure.figsize"] = (9.5, 4)
        self.fig, self.ax = plt.subplots(self.row, self.col,
                                         sharex='col', sharey='row', )
        self.axbig = self.fig.add_subplot(111, frameon=False)
        self.axbig.tick_params(labelcolor='none', which='both',
                               top='off', bottom='off',
                               left='off', right='off')
        self.axbig.grid(False)
        if r == 1 and c == 1:
            self.ax = np.array([self.ax]).reshape(-1, 1)
        elif r == 1 or c == 1:
            self.ax = self.ax.reshape((r, c))
        self.fig.subplots_adjust(wspace=0.0, hspace=0.0)
        
        self.legends = ([], [])
        self.datasets_styles = {}         
        self.subd = np.empty((self.row, self.col), object)
        self.thiscolor = 0
        for i, j in itertools.product(range(r), range(c)):
            self.subd[i, j] = {}            
        self.colorcheck = [mpl.colors.to_rgb(i) for i in bgcolor]
        self.whitelist = ['samplename']
        return
    
    def plot_data(self, scanname, Meas, Calc=None, Diff=None, 
                  meas =True, calc=False, diff=False, 
                  r=0, c=0, scal=1, offsetx=0, offsety=0, diffoffset=None, 
                  **kwargs):
        """Plot data.

        Parameters:
        -------------
        scanname: str
            The scanname from the data dictionary generated by the data_dict.
        Meas: data array
            The Measured data from the data dictionary.
        Calc and Diff:
            The Calculated and Diff data from the data dictionary. 
            The default values assume the data dictionary doesn't contain these
            two data. When the data dictionary has them, you can plot them by 
            setting calc = True, diff = True. Note the case difference here. 
        meas, calc, diff: bool
            True -- these curves from the data dictionary will be plotted. 
            False -- the curve will not be plotted. 
        r and c: int
           Optional when figure has a sinlge plot.
           r and c refers to the subpolot postition of
           where the data is being plotted.
           Default position is subplot(0,0) if the figure has multi subplots.
        scal:float, optional
            scaling factor for the y range of data in plotting.
            Default value is 1 as no scaling is applied.
        offsetx: float, optional
            the amount of offset on x axis when plot data.
        offsety: float, optional
            the amount of offset on y axis when plot data.
        diffoffset: float, optional
            the RELATIVE y axis distance by which the Diff data is away from 
            the Meas and the Calc data. 
            For example:
                diffoffset = -4 -- Diff curve is 4 units below the Meas/Calc.  
                diffoffset = 0 -- Diff curve is at the same y position as 
                                  the Meas / Calc curve. 
        **kwargs: dict
            kwargs passed to plt.plot
            
        Raises:
        --------
        AssertionError: when Calc (or Diff) curve is turned on but the 
                        data dictionary doesn't have the Calc (or Diff) data.

        Return:
        --------
        A updated figure.
        """
        for k in self.whitelist:
            kwargs.pop(k)
        styling = self.datasets_styles.get(scanname, kwargs)
        styling['color'] = styling.get('color', bgcolor[self.thiscolor])        
        kwargs.update({'color':styling['color']})
        self.datasets_styles.update({scanname:styling})
        line_name = scanname
        if scal != 1:
            line_name = '%s x%.2f' % (scanname, scal)
        if meas == True:
            line, = self.ax[r, c].plot(Meas[0] + offsetx, Meas[1] * scal + offsety, 
                                   label=line_name, **kwargs)  
        if line_name not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append(line_name)
        color = mpl.colors.to_rgb(kwargs['color'])
        if color in self.colorcheck:
            self.thiscolor = self.colorcheck.index(color)
            self.thiscolor = (self.thiscolor + 5) % 12
        data_in_plot={}
        data_in_plot[line_name +'_Meas'] = (Meas[0] + offsetx, 
                                           Meas[1] * scal + offsety)      
        if calc == True:
            assert Calc, "%r Data set doesn't have Calc data." % scanname
            line, = self.ax[r, c].plot(Calc[0] + offsetx, 
                                       Calc[1]* scal + offsety, 
                                       color = 'r', label=line_name +' Fit')
            data_in_plot[line_name +'_Calc'] = (Calc[0] + offsetx, 
                                               Calc[1] * scal + offsety)
        if diff == True:
            assert Diff, "%r Data set doesn't have Diff data." % scanname
            if diffoffset == None:
                if len(data_in_plot) == 1:
                    h = data_in_plot[line_name +'_Meas'][1].max()
                    l = data_in_plot[line_name +'_Meas'][1].min()
                if len(data_in_plot) == 2:
                    h = max(data_in_plot[line_name +'_Meas'][1].max(), 
                            data_in_plot[line_name +'_Calc'][1].max())
                    l = min(data_in_plot[line_name +'_Meas'][1].min(), 
                            data_in_plot[line_name +'_Calc'][1].min())
                amp = h - l
                diffoffset = l - (Diff[1].max()*scal+offsety) - amp * 0.04
            diffy = Diff[1]* scal + offsety + diffoffset
            diffdata = (Diff[0], diffy)
            line, = self.ax[r, c].plot(Diff[0] + offsetx, 
                                       Diff[1]* scal + + offsety + diffoffset, 
                                       color = 'g', label=line_name+' Diff')
            data_in_plot[line_name +'_Diff'] = diffdata
        self.add_data(r, c, **data_in_plot)
        return
    
    def config(self, context='', legend ='in', **kwargs):
        """configure the data. Call at the last step in plotting. For exameple, 
        plot the data by plot_data(**my_data_dictionary), then config(). 

        Parameters:
        -------------
        context: str
            Context where the plot will be used. 
            Value choices are:
                "manu" -- manuscription. 
                "pres" -- presentation. (to be continued on this context)
        legend: str, optional
            Include the legend in the plot.
            Value choices: 
                "in" -- put legend with each panel.
                "out" -- put an overall lengend outside of the panel. 
        **kwargs: dict
            kwargs passed to label() and title(). 
            See label() and title() for details.  

        Return:
        --------
        A updated figure.
        """
        if context == 'manu':
            legend=None
        self.ticks()
        self.legend(legend)
        self.label(**kwargs)
        self.title(**kwargs)
        return

    def add_data(self, r, c, **data_in_plot): 
        """helper method for plotData() to update subd.
        
        Return:
        --------
        subd: ndarray
            updated subd.
        """
        self.subd[r, c].update(data_in_plot)
        return self.subd

    def curves_diff(self, data_dict1=None, data_dict2=None, which_diff='Meas', 
                    r=0, c=0, scal=1, offsety=None, label=None, **kwargs):
        """Calculate the difference curve between data_dict1 and data_dict2. 
        Can be used to calcualte the Meas, Calc, or Diff difference between the
        2 data dictionaries, if both have all these data. When the either one of
        the two data_dicts is missing, the operation will be applied on existing 
        curves in the current panel. 
        
        Parameters:
        -------------
        data_dict1, data_dict2: data dictionaries generated by data_dict()
            The two data dictionaries between which the difference curve is 
            calculated. 
            The operation will be applied on the existing curves 
            in the current panel when either one argument is missing.
        r and c: int
           r and c refers to the subpolot postition to plot the curve.
        which_diff: str
                "Meas" (Default) -- plot difference between the two Meas data. 
                "Calc" -- plot difference between the two Calc data.
                "Diff" -- plot difference between the two Diff data.
                Note the case must match the keys in data dictionary. 
        scal: float
            to scal the difference curve by a factor of scal
        offsety:float, optional
            The EXACT y offset from the x-axis. 
            For example:
                diffoffset = -4 -- the Diff curve is along y= -4
                diffoffset = 0 -- the Diff curve is along y = 0 
            The default position is below the lower curve.
        label: str, optional
            The name of this difference curve to be included in the legend. 
            Default name is "Diff between data_name1 and data_name2. 
            E.g. 'Diff between data1 Meas and data2 Meas'.  
        **kwargs: dict
           kwargs passed to plt.plot
        
        Raises:
        --------
        AssertionError: when the 2 data ditionary arguments are not provided 
                        and the current panel doesn't have exactly 2 curves 
                        for the calculation.
        KeyError: when user wants to calculate the difference between the Calc(
                  or Diff) curves from the two different data dictionary, 
                  but either one or both data dictionaries don't have the Calc 
                  or Diff data. 
                  Note you will have to go back to check which data dictionary 
                  lacks of the data, there is no such an examination here. 
           
        Return:
        --------
        A updated figure.
        """
        if data_dict1 == None or data_dict2 == None:
            print("This operation needs 2 data sets, you don't provide enough.\
                  Now this operation is applied on the 2 curves in the \
                  current panel.")
            assert len(self.subd[r, c])==2,\
            "panel[%d, %d] must have excatly 2 data sets for this operation.\
            Or you can take 2 data sets of your choice to calculate." %(r, c)
            datalist = list( self.subd[r, c].values() )
            data1 = datalist[0]
            data2 = datalist[1]
            namelist = list( self.subd[r, c].keys() )
            line_name = 'Diff between %s and %s' %(namelist[0], namelist[1])
            line_name = '%s x%.2f' % (line_name, scal)
        else:
            try:
                data1 = data_dict1[which_diff]
                data2 = data_dict2[which_diff]
            except KeyError as e:
                print('The %s data is not in your data dictionary, \
                  please ensure both the 2 dictionaries \
                  have this key'.format(e.args[0]) %which_diff)
                return
            else:
                line_name = 'Diff between %s and %s' %(data_dict1['scanname']+
                        ' '+which_diff, data_dict2['scanname']+' '+which_diff)
                line_name = '%s x%.2f' % (line_name, scal)
        
        assert np.all(data1[0]==data2[0]),\
        "The 2 data sets don't have same x points."
                
        diffy =(data1[1] - data2[1])
        if offsety == None:
            h = max( data1[1].max(), data2[1].max() )
            l = min(data1[1].min(), data2[1].min())
            amp = h - l
            offsety = l - diffy.max()*scal - amp*0.04
        diffy = diffy*scal + offsety
        diffdata = (data1[0], diffy)
        if label == None:
            label = line_name
        color = kwargs.get('color', 'g')
        line = kwargs.get('linestyle', '-')
        marker = kwargs.get('marker', None)
        line, = self.ax[r, c].plot(diffdata[0], diffdata[1], 
                       label = label, color = color, linestyle = line, 
                       marker = marker)
        if label not in self.legends[1]:
            self.legends[0].append(line)
            self.legends[1].append(label)
        data_in_plot = {label: diffdata}   
        self.add_data(r, c, **data_in_plot)
        return

    def ticks(self):
        """helper method for plotData() to remove the overlapping ticks."""
        nbins = 6
        for i, j in itertools.product(range(self.row), range(self.col)):
            xl, xh, yl, yh = [], [], [], []
            yl.append(self.ax[i, j].axis()[2])
            yh.append(self.ax[i, j].axis()[3])
            xl.append(self.ax[i, j].axis()[0])
            xh.append(self.ax[i, j].axis()[1])
            xmin, xmax, ymin, ymax = min(xl), max(xh), min(yl), max(yh)
            self.ax[i, 0].set_ylim(round((ymin ), 2),
                                   round((ymax ), 2)) 
            self.ax[i, 0].yaxis.set_major_locator( \
                MaxNLocator(nbins, prune='both'))
            self.ax[-1, j].set_xlim(np.floor(np.array(xmin).min()),
                                    np.ceil(np.array(xmax).max()))
            self.ax[-1, j].xaxis.set_major_locator( \
                MaxNLocator(nbins, prune='both'))
        return

    def label(self, x='r', xunit='AA', y='G', yunit='AA^{-2}', label_math=True, 
              **kwargs):
        """Method to generate labels for axis in the overall plot.

        Parameters:
        -------------
        x: str, optional
          the label for x axis. Default value is 'r' as in a G(r) plot
        xunit: str, optional
          unit for the x axis.
          Default value is 'AA', a Latex command for Angstrom.
          To see this Math symbol, the 'math' parameter has to be 'True'.
        y: str, optional
          the label for y axis. Default value is 'G' as in a G(r) plot
        yunit: str, optional
          unit for the y axis.
          Default value is 'AA^{-2}' for G(r)
          a Latex command for the inverse square of Angstrom.
          To see the Math symbol, the 'math' parameter has to be 'True'.
        label_math: bool, optional
          Ture: default value. Turn on the math expression for the labels.
          False: write the labels as normal text.
        """        
        if label_math:
            xl = r'$\mathrm{%s}\  \mathrm{( \%s )}$' % (x, xunit)
            yl = r'$\mathrm{%s}\  \mathrm{( \%s )}$' % (y, yunit)
        else:
            xl = '%s (%s)' % (x, xunit)
            yl = '%s (%s)' % (y, yunit)
        self.axbig.set_xlabel(xl)
        self.axbig.set_ylabel(yl)
        if self.row > self.col:
            self.axbig.yaxis.set_label_coords(-0.166, 0.5)
        elif self.row < self.col:
            self.axbig.yaxis.set_label_coords(-0.096, 0.5)
        else:
            self.axbig.yaxis.set_label_coords(-0.11, 0.5)
        return

    def title(self, title='', title_math=False, **kwargs):
        """Method generate labels for axis.

        Parameters:
        -------------
        t: str, optional
         the tile of the overal plot.
         Default to be empty.
        title_math: bool, optional
          Ture: Turn on the math expression for the labels.
          False: default. Write the labels as normal text.
        """
        if title_math:
            title = r'$\mathrm{%s} $' % title
        return self.axbig.set_title(title)

    def legend(self, disp=None):
        """Method to create legend for the figure.

        Parameters:
        -------------
        disp: str, optional
            Chose if the legend is outside or inside of the plotting area.
            "None": default value. No legend on the plot.
            "out": an overall outside legend for all lines in the figure
            "in": each subplot has its own legend.
        """
        if disp:
            if disp == 'out':
                self.legend_out()
            if disp == 'in':
                self.legend_in()
        return

    def legend_out(self):
        """helper method for the legend(), creating an overall legend
        for all lines. The legend is outside of the plotting box."""
        return plt.legend(self.legends[0], self.legends[1], loc='center left',
                          bbox_to_anchor=(1, 0.6), borderaxespad=0, \
                          labelspacing=1., prop={'size': 8}, handlelength=3)

    def legend_in(self):
        """helper method for the legend(),
        creating legends inside of each subplot."""
        for i, j in itertools.product(range(self.row), range(self.col)):
            self.ax[i, j].legend(loc='best', labelspacing=1.,
                                 prop={'size': 8}, handlelength=3)
        return

    def save(self, name="myplot", form="pdf"):
        """Save the plot to the current working diretory.

        Parameters:
        -------------
        name: str
            the name of plot being saved.
        form:str, optional
            the form of figure file. Example, png, eps, pdf.
        """
        return self.fig.savefig('%s.%s' % (name, form))

    def show(self):
        """Show figure in a GUI window."""
        return plt.show()

    def figure_size(self, width, height):
        """Change the current figure shape or size"""
        self.fig.set_figwidth(width)
        self.fig.set_figheight(height)
        return

    def set_xlim(self, col, low, high):
        """ a method to manually set the x range in plot.

        Parameters:
        -------------
        col: int
            the column at which the shared x-axis limit should be set.
        low: float
            the lower bound of the x-axis being set.
        high: float
            the higher bound of the x-axis being set.
        """
        return self.ax[0, col].set_xlim([low, high])

    def set_ylim(self, row, low, high):
        """ a method to manually set the shared y range in the plot.

        Parameters:
        -------------
        row: int
            the row at which the shared y-axis limit should be set.
        low: float
            the lower bound of the y-axis being set.
        high: float
            the higher bound of the y-axis being set.
        """
        return self.ax[row, 0].set_ylim([low, high])