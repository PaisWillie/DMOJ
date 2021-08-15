# Problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        separated = [int(y) for y in str(n)]
        for x in separated:
            product *= x
        return product - sum(separated)
