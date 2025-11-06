class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if math.sqrt(num)==int(num**0.5) else False