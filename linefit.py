import numpy as np
def linefit(x,y,**kwargs):
    notnan=np.where((x==x) & (y==y))
    usex=np.array(x)[notnan]
    usey=np.array(y)[notnan]
    fit=np.polyfit(usex,usey,1,full=True,**kwargs)
    sse=np.sqrt(fit[1]/(len(usex)-2))
    mx=usex.mean()
    sx2=(np.array(usex-mx)**2).sum()
    err0=sse/np.sqrt(sx2)
    err1=sse*np.sqrt(1.0/len(usex)+mx*mx/sx2)
    return fit[0],[err0[0],err1[0]]
