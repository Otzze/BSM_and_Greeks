import math
from scipy.stats import norm

"""
    Black-Scholes-Merton (BSM) option pricing model
    @args:
        S: Current stock price
        K: Option strike price
        T: Time to expiration in years
        r: Risk-free interest rate
        sigma: Volatility of the underlying stock
    @returns:
        C: Call option price
        P: Put option price
"""
def compute_prices(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return float(C), float(P)

"""
    Compute the Greeks of the option
    @args:
        S: Current stock price
        K: Option strike price
        T: Time to expiration in years
        r: Risk-free interest rate
        sigma: Volatility of the underlying stock
        option_type: Type of option ('call' or 'put')
    @returns:
        delta: Delta of the option
        gamma: Gamma of the option
        theta: Theta of the option
        vega: Vega of the option
        rho: Rho of the option
"""
def compute_greeks(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if option_type == 'call':
        delta = norm.cdf(d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * norm.cdf(d2))
    elif option_type == 'put':
        delta = norm.cdf(d1) - 1
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) + r * K * math.exp(-r * T) * norm.cdf(-d2))
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * norm.pdf(d1) * math.sqrt(T)
    rho = K * T * math.exp(-r * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    return float(delta), float(gamma), float(theta), float(vega), float(rho)
