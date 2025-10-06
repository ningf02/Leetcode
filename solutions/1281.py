class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l1 = str(n)
        summ = sum(int(d) for d in l1)
        product = 1
        for d in l1:
            product *= int(d)
        return product - summ
        
