# https://leetcode.com/problems/two-sum/
import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]
                pass


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        tests = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]
        for nums, target, expected in tests:
            results = solution.twoSum(nums, target)
            with self.subTest(i=f"{nums=} {target=}"):
                self.assertEqual(sorted(results), sorted(expected))


if __name__ == "__main__":
    unittest.main()
