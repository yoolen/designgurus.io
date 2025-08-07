"""
Given a non-negative integer x, return the square root of x rounded down to the nearest
integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        For any number x, its square root will lie between 0 and x/2.
        Use binary search to find the closest integer rounded down.
        Find the bounds and then split the search space in half
        each time to see which half the square root might be in.
        """
        if x < 2:
            return x  # All x <= 1 are their own square root
        # For all other values iterate over the bounds until we arrive at a solution
        # or cross the bounds, at which point we know that the right bound was the
        # answer (since we are rounding down immediately).
        left, right = 0, x // 2
        # Bisect the data in half each time by searching the midpoint and then
        # assigning a new left or right. Since we're checking the midpoint we
        # already know that it can't be the answer and should offset by 1 more.
        while left <= right:
            midpoint = (left + right) // 2
            square = midpoint**2
            # Check which half of the remaining values contains x
            if x > square:
                left = midpoint + 1
            elif x < square:
                right = midpoint - 1
            else:
                return midpoint
        return right
