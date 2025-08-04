import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        After removing all punctuation and whitespace, use a two-pointer
        approach to iterate from the outside in and check that every character
        is paired with itself. Upon reaching the middle without any mismatches
        a palindrome is found.
        O(n) since we iterate over every element once (technically n/2 since
        we cover 2 characters on each pass).
        """
        normalized = "".join(
            char.lower()
            for char in s
            if char not in (string.punctuation + string.whitespace)
        )
        left, right = 0, len(normalized) - 1
        while left < right:
            if normalized[left] != normalized[right]:
                return False
            left += 1
            right -= 1
        return True
