"""
LeetCode 2469. Convert the Temperature
https://leetcode.com/problems/convert-the-temperature/

Difficulty: Easy

Problem
-------
You are given a non-negative floating point number `celsius`, representing a
temperature in Celsius. Convert it into Kelvin and Fahrenheit and return them
as a list `[kelvin, fahrenheit]`.

    Kelvin     = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00

Answers within 1e-5 of the actual values are accepted.

Example
-------
    Input:  celsius = 36.50
    Output: [309.65000, 97.70000]

Constraints
-----------
    0 <= celsius <= 1000

Complexity
----------
    Time:  O(1)
    Space: O(1)
"""

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]


if __name__ == "__main__":
    solution = Solution()

    # Basic sanity checks (compare with tolerance for floating point math)
    def close(a, b, tol=1e-5):
        return all(abs(x - y) <= tol for x, y in zip(a, b))

    assert close(solution.convertTemperature(36.50), [309.65000, 97.70000])
    assert close(solution.convertTemperature(122.00), [395.15000, 251.60000])
    assert close(solution.convertTemperature(0.00), [273.15000, 32.00000])

    print("All test cases passed.")
