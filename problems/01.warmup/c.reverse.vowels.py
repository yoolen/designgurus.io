"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper
cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Use a two-pointer approach that iterates from
        the outside in looking for vowels and swapping
        them as they are encountered. When the two indices
        converge the whole string has been swapped.
        O(n) since we are only iterating over the list once.
        """
        string = list(s)
        vowels = "aeiou"
        right = len(s) - 1
        for left, char in enumerate(string):
            if left >= right:
                break
            if char.lower() not in vowels:
                continue
            while string[right].lower() not in vowels and left < right:
                right -= 1
            string[left], string[right] = string[right], string[left]
            right -= 1
        return "".join(string)
