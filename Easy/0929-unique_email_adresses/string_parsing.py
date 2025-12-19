"""
Unique Email Addresses (LeetCode 929)
------------------------------------
This module provides a solution to count unique email addresses after
normalizing them according to specific rules.

Normalization rules:
1. In the local name, everything after a '+' is ignored.
2. All '.' characters in the local name are removed.
3. The domain name remains unchanged.

Example:
    Input:
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@leetcode.com"
        ]

    Output:
        1
"""


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        """
        Count the number of unique email addresses after normalization.

        Args:
            emails (list[str]): List of email address strings.

        Returns:
            int: Number of unique normalized email addresses.
        """
        unique_emails = set()

        for email in emails:
            at_index = email.find("@")
            local_name = email[:at_index]
            domain = email[at_index:]

            plus_index = local_name.find("+")
            if plus_index != -1:
                local_name = local_name[:plus_index]

            # Remove dots from the local name
            local_name = "".join(char for char in local_name if char != ".")

            unique_emails.add(local_name + domain)

        return len(unique_emails)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    emails1 = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@leetcode.com"
    ]
    print("Input:", emails1)
    print("Output:", solution.numUniqueEmails(emails1))
    print()

    # Example 2
    emails2 = [
        "a@leetcode.com",
        "b@leetcode.com",
        "c@leetcode.com"
    ]
    print("Input:", emails2)
    print("Output:", solution.numUniqueEmails(emails2))
    print()

    # Example 3
    emails3 = [
        "user.name+tag+sorting@example.com",
        "username@example.com",
        "user.name@example.com"
    ]
    print("Input:", emails3)
    print("Output:", solution.numUniqueEmails(emails3))
