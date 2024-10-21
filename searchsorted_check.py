import numpy as np

def searchsorted_check(a,v,side='left', sorter=None):
    result = np.searchsorted(a, v, side=side, sorter=sorter)

    w1=np.where(result<len(a))[0]
    w2=np.where(v[w1]==np.array(a)[result[w1]])[0]

    return w1[w2],result[w1[w2]]

def searchsorted_check_default(a,v,side='left', sorter=None,nomatch=-1):
    result = np.searchsorted(a, v, side=side, sorter=sorter)
    toreturn = np.zeros_like(result)+nomatch
    w1=np.where(result<len(a))[0]
    w2=np.where(v[w1]==np.array(a)[result[w1]])[0]
    toreturn[w1[w2]]=result[w1[w2]]
    return toreturn
