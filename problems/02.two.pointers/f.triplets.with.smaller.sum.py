class Solution:
    def searchTriplets(self, arr, target):
        """
        Find all triplets where arr[i] + arr[j] + arr[k] < target.

        Approach:
        1. Sort the array to enable two-pointer technique
        2. For each element at index i, use two pointers (left, right) to find
          valid pairs in the remaining array
        3. When arr[i] + arr[left] + arr[right] < target:
          - Due to sorting, we know arr[i] + arr[left] + arr[x] < target
            for all x between left+1 and right
          - Count all these valid pairs: right - left
          - Move left pointer forward to find more combinations
        4. When sum >= target, move right pointer left to get smaller values

        Time: O(n^2), Space: O(1) excluding sort
        """
        count = 0
        arr = sorted(arr)
        elements = len(arr)
        for i in range(elements - 2):
            left, right = i + 1, elements - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total < target:
                    # Found largest valid pairing for the given left value so we know
                    # that any right value to the left (left + 1, left + 2, ..., right)
                    # is valid and can count them all at once
                    count += right - left
                    left += 1  # go to the next left
                else:
                    right -= 1

        return count
