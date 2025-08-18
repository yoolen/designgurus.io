class Solution:
    def sort(self, arr):
        """
        Sort an array in-place containing only three distinct values (0, 1, 2).
        Also known as the Dutch National Flag problem.

        Approach (Three-pointer technique):
        1. Use three pointers:
           - i: current element being processed
           - low: boundary for 0s (next position to place a 0)
           - high: boundary for 2s (next position to place a 2)

        2. Process elements until i crosses the high boundary:
           - If arr[i] == 0: swap with arr[low], increment both low and i
           - If arr[i] == 1: leave in place, increment i only
           - If arr[i] == 2: swap with arr[high], decrement high only
             (don't increment i since we need to process the swapped element)

        Result: [all 0s][all 1s][all 2s]

        Time: O(n), Space: O(1)
        """
        i, low, high = 0, 0, len(arr) - 1
        while i <= high:
            if arr[i] == 1:
                i += 1
            elif arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
                i += 1
            else:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1

        return arr
