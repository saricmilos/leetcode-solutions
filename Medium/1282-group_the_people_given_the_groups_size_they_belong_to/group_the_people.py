"""
group_people.py

Module to group people based on the size of groups they belong to.

Example:
    >>> from group_people import Solution
    >>> sol = Solution()
    >>> sol.groupThePeople([3,3,3,3,3,1,3])
    [[0, 1, 2], [3, 4, 6], [5]]
"""

from typing import List


class Solution:
    """
    Solution for grouping people by their group sizes.

    Methods
    -------
    groupThePeople(groupSizes: List[int]) -> List[List[int]]:
        Groups people according to the size specified for each person.
    """

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        Group people based on the group size they belong to.

        Parameters
        ----------
        groupSizes : List[int]
            A list where groupSizes[i] is the size of the group person i belongs to.

        Returns
        -------
        List[List[int]]
            A list of groups, each group is represented as a list of indices.
        """
        groups = {}  # size -> list of people waiting for that size
        result = []

        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []

            groups[size].append(i)  # add person to the bucket

            # if bucket reaches required size, form a group
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []  # reset for the next group

        return result


if __name__ == "__main__":
    # Example usage
    sol = Solution()
    example_input = [3, 3, 3, 3, 3, 1, 3]
    output = sol.groupThePeople(example_input)
    print(f"Input: {example_input}")
    print(f"Grouped Output: {output}")
