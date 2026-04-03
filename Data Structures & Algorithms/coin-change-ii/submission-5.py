class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 可以使用 i 以及 i 之前的所有硬幣
        # j: target amount
        ways = [0] * (amount + 1)
        ways[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                ways[j] += ways[j-coin]

        return ways[amount]


        