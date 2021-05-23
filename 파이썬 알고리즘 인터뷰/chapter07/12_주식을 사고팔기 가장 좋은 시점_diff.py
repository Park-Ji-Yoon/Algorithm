import sys

def maxProfit(prices):
  profit = 0
  min_price = sys.maxsize # system상 가장 큰 값

  # 최댓값과 최솟값을 갱신
  for price in prices:
    min_price = min(min_price, price) # 원래 min_price와 price 중 작은 것
    profit = max(price - min_price, profit) # 원래 profit과 price에서 min_price중 큰 것

  return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))