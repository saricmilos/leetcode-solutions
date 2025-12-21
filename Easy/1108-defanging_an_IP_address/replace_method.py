# defang_ip_address.py

class Solution:
    """
    Solution for LeetCode 1108: Defanging an IP Address.

    Given a valid IPv4 address, this class returns a "defanged" version
    where every period '.' is replaced with '[.]'.
    """

    def defangIPaddr(self, address: str) -> str:
        """
        Defangs the given IPv4 address by replacing '.' with '[.]'.

        Args:
            address (str): A valid IPv4 address.

        Returns:
            str: The defanged IP address.
        """
        return address.replace(".", "[.]")


def main() -> None:
    """
    Demonstrates usage of the Solution class with example inputs.
    """
    solution = Solution()

    # Example 1
    ip = "192.168.0.1"
    result = solution.defangIPaddr(ip)
    print(f"Input: {ip} -> Defanged: {result}")  # Expected Output: "192[.]168[.]0[.]1"

    # Example 2
    ip = "127.0.0.1"
    result = solution.defangIPaddr(ip)
    print(f"Input: {ip} -> Defanged: {result}")  # Expected Output: "127[.]0[.]0[.]1"


if __name__ == "__main__":
    main()
