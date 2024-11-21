# Trend Convexity
## Background
This repository replicates the results within [_Tail protection for long investors: Trend convexity at work_](https://arxiv.org/abs/1607.02410) by J.P. Bouchaud et. al. The repo analysis Trend Follower CTA strategies and their analogous relationship to long-convexity strategies such as long straddles. Historically this relationship is well known since buy straddles essentially buys volatility (both upside and downside). 

## CTA Performance
Historically Hedge Fund performance has slight negative convexity to SPX
![image](https://github.com/diegodalvarez/TrendConvexity/assets/48641554/d91e98d9-cd4b-4138-9808-51e7bbd1b30c)

Hedge Fund CTA indices have positive convexity to markets although very slightly
![image](https://github.com/diegodalvarez/TrendConvexity/assets/48641554/08113a9c-165c-4a4f-9f6f-a749a4417fe2)

## Trend of Single Asset
Creating a signature plot of each asset class it appears that there is trend to harvest
![image](https://github.com/user-attachments/assets/02de2b51-1b31-4277-9822-7c9e416ba5d1)

First start by normalizing returns so they have unit variance using differenced price and lagged EWM standard deviation
```math
\begin{equation}
R_t = \frac{D_t}{\sigma_{t-1}} \; \textrm{where} \; \sigma_t := \gamma \sqrt{\mathscr{L}_{\tau_\sigma}[D_t^2]}
\end{equation}
```
Then the aggregate PnL $(G_t)$ over some period $\tau'$ is proportfolio to its long term volatility over period $\tau$ and its 1 day volatility (which is 1 because its unit variance). In this case $\tau' \thickapprox \frac{\tau}{2}$. 
```math
\mathcal{L}_{\tau'}[G_t] = \frac{\lambda \tau}{\tau - 1} \left( \tau \mathcal{L}_{\tau}^2 [R_t] - \mathcal{L}_{\tau'}[R_t^2] \right)
```
Using SPX roll adjusted futures with trend determined by the sign of EWMA returns over a period $\tau$ yields
![image](https://github.com/user-attachments/assets/be712b6f-8b21-4b61-9306-94ae5e144932)

Now plotting the cumulative sum over period $\tau'$ vs the signal gives
![image](https://github.com/user-attachments/assets/5eb52e1b-3939-42ab-afa1-ee1a339886d8)
