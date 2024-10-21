import numpy as np
from numpy import nanmedian,nanmean
def bindata(xdata,ydata,bins,median=0,samplestd=0,logdiff=0,logerr=0,xerrsize=100,xmedian=0,**kwargs):
    dg=np.digitize(xdata,bins,**kwargs)
    yarr=np.array(ydata)
    ybins=np.array([])
    binerr=np.array([])
    xbins=np.array([])
    xlower=[]
    xuper=[]
    npts=[]
    for i in range(len(bins)-1):
        w=np.where(dg==i+1)[0]
        wnotnan=np.where((np.isfinite(xdata[w])) & (np.isfinite(ydata[w])))[0]
        npts.append(len(wnotnan))
        if(len(w)==0):
            xbins=np.append(xbins,np.nan)
            if xerrsize!=100:
                xlower.append(np.nan)
                xuper.append(np.nan)
            ybins=np.append(ybins,np.nan)
            binerr=np.append(binerr,np.nan)
        elif(len(w)==1):
            xbins=np.append(xbins,xdata[w])
            if xerrsize!=100:
                xlower.append(xbins[i])
                xuper.append(xbins[i])
            if(median==1):
                ybins=np.append(ybins,nanmedian(yarr[w]))
            else:
                ybins=np.append(ybins,np.nanmean(yarr[w]))
            binerr=np.append(binerr,np.nan)
        else:
            if xmedian==1:
                xbins=np.append(xbins,nanmedian(xdata[w]))
            else:
                xbins=np.append(xbins,nanmean(xdata[w]))
            if xerrsize!=100:
                xlower.append(np.percentile(xdata[w[wnotnan]],50-xerrsize/2.0))
                xuper.append(np.percentile(xdata[w[wnotnan]],50+xerrsize/2.0))
            if(median==1):
                ybins=np.append(ybins,nanmedian(yarr[w]))
                if(samplestd!=0):
                    binerr=np.append(binerr,np.nanstd(yarr[w]))
                else:
                    binerr=np.append(binerr,1.253*np.nanstd(yarr[w])/np.sqrt(len(w)))
            else:
                ybins=np.append(ybins,np.nanmean(yarr[w]))
                if(samplestd!=0):
                    binerr=np.append(binerr,np.nanstd(yarr[w]))
                else:
                    binerr=np.append(binerr,np.nanstd(yarr[w])/np.sqrt(len(w)))
    if xerrsize==100:
        if logdiff != 1:
            xlowerr=[xbins[i]-bins[i] for i in range(len(xbins))]
            xuperr=[bins[i+1]-xbins[i] for i in range(len(xbins))]
        else:
            xlowerr=[10**xbins[i]-10**bins[i] for i in range(len(xbins))]
            xuperr=[10**bins[i+1]-10**xbins[i] for i in range(len(xbins))]
    else:
        if logdiff != 1:
            xlowerr=[xbins[i]-xlower[i] for i in range(len(xbins))]
            xuperr=[xuper[i]-xbins[i] for i in range(len(xbins))]
        else:
            xlowerr=[10**xbins[i]-10**xlower[i] for i in range(len(xbins))]
            xuperr=[10**xuper[i]-10**xbins[i] for i in range(len(xbins))]
    if logerr != 1:
        binerr=np.array([binerr,binerr])
    else:
        binlower=[10**ybins[i]-10**(ybins[i]-binerr[i]) for i in range(len(ybins))]
        binupper=[10**(ybins[i]+binerr[i])-10**ybins[i] for i in range(len(ybins))]
        binerr=np.array([binlower,binupper])
    return ybins,binerr,xbins,np.array([xlowerr,xuperr]),np.array(npts)
