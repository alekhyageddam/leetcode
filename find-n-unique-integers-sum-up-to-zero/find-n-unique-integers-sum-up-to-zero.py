class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []
        #if n is odd
        if n%2 != 0:
            a.append(0)
        for i in range(1, n):
            if len(a) == n:
                break
            a.append(-i)
            a.append(i)
        return a 