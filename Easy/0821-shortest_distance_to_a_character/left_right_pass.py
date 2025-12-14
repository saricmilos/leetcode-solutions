class Solution:
    """
    LeetCode 821. Shortest Distance to a Character

    Given a string `s` and a character `c`, return an array where each element
    represents the shortest distance from that position to the character `c`.

    Approach:
    - First pass (left → right): track the most recent occurrence of `c` on the left.
    - Second pass (right → left): track the most recent occurrence of `c` on the right.
    - For each index, take the minimum of both distances.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0] * n

        # Left → Right pass
        last_seen_left = float('-inf')
        for i in range(n):
            if s[i] == c:
                last_seen_left = i
            answer[i] = abs(i - last_seen_left)

        # Right → Left pass
        last_seen_right = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_seen_right = i
            answer[i] = min(answer[i], abs(i - last_seen_right))

        return answer


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s = "loveleetcode"
    c = "e"
    print(sol.shortestToChar(s, c))
    # Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    # Example 2
    s = "aaab"
    c = "b"
    print(sol.shortestToChar(s, c))
    # Output: [3, 2, 1, 0]
