def sumNums(num:int) -> int:
    ans = 0
    num = str(num)
    for digit in num:
        ans += int(digit) ** 2
    return ans


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            else:
                seen.add(n)
                n = sumNums(n)
        return True