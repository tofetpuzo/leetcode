from typing import List


def cheapFlights(nodes: int, flights: List[List[int]], dist: int, src: int, k: int):
    prices = [float("inf")] * nodes
    prices[src] = 0

    for _ in range(k + 1):
        tmpPrices = prices.copy()
        for sr, dis, price in flights:  # src: source, dist = destination, price
            if prices[sr] == float("inf"):
                continue
            if prices[sr] + price < prices[dis]:
                tmpPrices[dis] = prices[sr] + price

        prices = tmpPrices

    return -1 if prices[dist] == float("inf") else prices[dist]


prices = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dist = 2
k = 1
n = 3
print(cheapFlights(src=src, nodes=n, k=k, dist=dist, flights=prices))
