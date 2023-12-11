# Trend Convexity
## Background
This repository replicates the results within [_Tail protection for long investors: Trend convexity at work_](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2777657) by J.P. Bouchaud et. al. The repo analysis Trend Follower CTA strategies and their analogous relationship to long-convexity strategies such as long straddles. Historically this relationship is well known since buy straddles essentially buys volatility (both upside and downside). 

## CTA Performance
Historically Hedge Fund performance has slight negative convexity to SPX
![image](https://github.com/diegodalvarez/TrendConvexity/assets/48641554/d91e98d9-cd4b-4138-9808-51e7bbd1b30c)

Hedge Fund CTA indiices have positive convexity to markets although very slightly
![image](https://github.com/diegodalvarez/TrendConvexity/assets/48641554/08113a9c-165c-4a4f-9f6f-a749a4417fe2)

## Trend of Single Asset
We can model the PnL of trend as 
$$\mathcal{L_t}(X_t) := (1 - \alpha) \sum_{i \le t} \alpha^{(t-1)} X_i \newline$$
$$\alpha := 1 - \frac{2}{\tau  + 1}$$
![image](https://github.com/diegodalvarez/TrendConvexity/assets/48641554/3369def5-c2cd-4c01-bd1a-ff00c09a5110)
