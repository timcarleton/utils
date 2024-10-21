import matplotlib.pyplot as plt
import numpy as np
def histogramcontour(x,y,bins=[20,20],range=None,density=False,weights=None,fill=False,ax=None,**args):
    h2,xh,yh=np.histogram2d(x,y,bins=bins,range=range,density=density,weights=weights)
    xpts=np.linspace(min(xh),max(xh),num=len(xh)-1)
    ypts=np.linspace(min(yh),max(yh),num=len(yh)-1)
    if not fill:
        if ax==None:
            plt.contour(xpts,ypts,h2.transpose(),**args)
        else:
            ax.contour(xpts,ypts,h2.transpose(),**args)
    else:
        if ax==None:
            plt.contourf(xpts,ypts,h2.transpose(),**args)
        else:
            ax.contourf(xpts,ypts,h2.transpose(),**args)
    return h2,xh,yh
