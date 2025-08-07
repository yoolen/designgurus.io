"""
A pangram is a sentence where every letter of the English alphabet appears at least
once.

Given a string sentence containing English letters (lower or upper-case), return true if
sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces, your
solution should handle these too.
"""


class Solution:
    def checkIfPangram(self, sentence):
        """
        After removing all whitespace and non-alphabetical characters,
        check if the count of unique characters (ignoring case) is
        exactly the same as the number of characters in the English
        alphabet.
        O(n) since we are only iterating over the list once.
        """
        return (
            len(set("".join([char.lower() for char in sentence if char.isalpha()])))
            == 26
        )
