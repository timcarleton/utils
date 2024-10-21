import scipy.stats.distributions as dist
def getbinomconf(k,n,c=0.5):
    p_lower=dist.beta.ppf((1-c)/2.,k+1,n-k+1)
    p_upper = dist.beta.ppf(1-(1-c)/2.,k+1,n-k+1)
    return p_lower,p_upper
