"""
Given a sorted array, create a new array containing squares of all the numbers of the
input array in the sorted order.
"""


class Solution:
    def makeSquares(self, arr):
        """
        Since the sorted array can contain negative values and we know that
        the square of negative values is a positive, the "middle values" of
        the array will be less than the ends. Working from outside in from
        the ends of the array, insert the squares in reverse order, comparing them
        as we iterate inwards.
        """
        n = len(arr)
        squares = [0 for x in range(n)]
        left, right = 0, n - 1
        for i in range(right, -1, -1):  # insert largest to smallest
            if (l_sq := arr[left] ** 2) > (r_sq := arr[right] ** 2):
                squares[i] = l_sq
                left += 1
            else:
                squares[i] = r_sq
                right -= 1

        return squares
