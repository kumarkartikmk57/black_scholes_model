import numpy as np
from scipy import stats
from numpy import log,exp,sqrt


def call_option(S,E,T,rf,sigma):
    #s=stock_price,E=strike_price,T=time_expiry,rf=risk_free
    d1 = (log(S/E)+(rf+sigma*sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    print("The value of d1 is ",d1)
    print("The value of d2 is ",d2)
    pv = S*stats.norm.cdf(d1)-E*exp(-rf*T)*stats.norm.cdf(d2)
    print("The present value of strike price is ",pv)
    return pv

def put_option(S,E,T,rf,sigma):
    #s=stock_price,E=strike_price,T=time_expiry,rf=risk_free

    d1 = (log(S/E)+(rf+sigma*sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    print("The value of d1 is ",d1)
    print("The value of d2 is ",d2)
    pv = -S*stats.norm.cdf(-d1)+E*exp(-rf*T)*stats.norm.cdf(-d2)
    print("The present value of strike price is ",pv)

#underlying stock price at T=0
S0=int(input("ENter stock value "))
#strike price
E=int(input("ENter strike price "))
#time_expiry
T=int(input("Enter time of maturity "))
#risk_free
rf = 0.05
#volatility of underlying stock
sigma = 0.2
call_option(S0,E,T,rf,sigma)
put_option(S0,E,T,rf,sigma)

