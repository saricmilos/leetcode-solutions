class Solution:
    """
    A class to merge two strings alternately.

    Methods
    -------
    mergeAlternately(word1: str, word2: str) -> str
        Returns a single string by alternating characters from word1 and word2.
        If one string is longer, appends the remaining characters at the end.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately.

        Parameters
        ----------
        word1 : str
            The first string.
        word2 : str
            The second string.

        Returns
        -------
        str
            The merged string with alternating characters from word1 and word2.
            Remaining characters of the longer string are appended at the end.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.mergeAlternately("abc", "pqr")
        'apbqcr'
        >>> sol.mergeAlternately("abc", "pqrst")
        'apbqcrst'
        >>> sol.mergeAlternately("abcd", "pq")
        'apbqcd'
        """
        result = []
        n1, n2 = len(word1), len(word2)
        for i in range(max(n1, n2)):
            if i < n1:
                result.append(word1[i])
            if i < n2:
                result.append(word2[i])
        return ''.join(result)


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    examples = [
        ("abc", "pqr"),
        ("abc", "pqrst"),
        ("abcd", "pq"),
    ]

    for w1, w2 in examples:
        merged = sol.mergeAlternately(w1, w2)
        print(f'mergeAlternately("{w1}", "{w2}") -> "{merged}"')
