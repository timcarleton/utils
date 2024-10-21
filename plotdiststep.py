import matplotlib.pyplot as plt
import numpy as np
def plotdiststep(bins,values,edge=0,plotedge=False,**kwargs):
    if plotedge:
        plt.step(np.hstack([bins[0],bins,bins[-1]]),np.hstack([edge,values,values[-1],edge]),where='post',**kwargs)
    else:
        plt.step(np.hstack([bins]),np.hstack([values,values[-1]]),where='post',**kwargs)
        
