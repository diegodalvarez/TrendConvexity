# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:01:31 2024

@author: Diego
"""

import numpy as np
import pandas as pd

class Heteroskedasticity:
    
    def _alpha(self, tau: float) -> float: return(1 - (2 / (tau - 1)))
    
    def Lt(self, Xt: pd.Series, tau: float) -> pd.Series:
    
        alpha = self._alpha(tau)
        result = 0
        t = len(Xt) + 1
        
        for i in range(1, t + 1): result += alpha **(t-i) * Xt[i-2]
        return (result * (1 - alpha))

    def _sigmat(self, Xt: pd.Series, gamma: float, tau: float) -> float: return(gamma * np.sqrt(self.Lt(Xt ** 2, tau)))
    
    def sigmat(self, Xt: pd.Series, gamma: float = 1.05, tau: float = 10) -> pd.Series: 
    
        out = []
        for i in range(len(Xt)): 
    
            xt = Xt.iloc[:i+1]
            sigma = self._sigmat(xt, gamma, tau)
            out.append(sigma)
    
        out_series = pd.Series(
            data = out,
            index = Xt.index)
        
        return out_series
    
    def _Ltau(self, Xt: pd.Series, tau: float) -> float:
        
        lambda_ = 0.01 / np.sqrt(tau)
        constant = (lambda_ * tau) / (tau - 1)
        tau_prime = (tau / 2) + (1 / (2 * tau))
        out = constant * (tau * (self.Lt(Xt, tau) ** 2) - self.Lt(Xt ** 2, tau_prime))
        
        return out
    
    def Ltau(self, Xt: pd.Series, tau: float, verbose = False) -> pd.Series:
        
        if verbose == True: 
            
            print("Working on Ltau")
            mod_check = (int(len(Xt) / 1000) * 100)
        
        out = []
        for i in range(len(Xt)): 
    
            xt = Xt.iloc[:i+1]
            ltau = self._Ltau(Xt = xt, tau = tau)
            out.append(ltau)
            
            if verbose == True and i % mod_check == 0: print("Working on", i)
    
        out_series = pd.Series(
            data = out,
            index = Xt.index)
        
        if verbose == True: print("\n")
        
        return out_series
    
    def _past_trend(self, Xt: pd.Series, tau: float) -> float: return(np.sqrt(tau) * self.Lt(Xt = Xt, tau = tau))
    
    def past_trend(self, Xt: pd.Series, tau: float, verbose = False) -> pd.Series:
        
        if verbose == True: 
            
            print("Working on Past Trend")
            mod_check = (int(len(Xt) / 1000) * 100)
        
        out = []
        for i in range(len(Xt)): 
    
            xt = Xt.iloc[:i+1]
            t = self._past_trend(Xt = xt, tau = tau)
            out.append(t)
            
            if verbose == True and i % mod_check == 0: print("Working on", i)
    
        out_series = pd.Series(
            data = out,
            index = Xt.index)
        
        if verbose == True: print("\n")
        
        return out_series