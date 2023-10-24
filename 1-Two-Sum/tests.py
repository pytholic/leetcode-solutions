import pytest
from twosum import Solution

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize("nums, target, expected", test_cases)
def test_twoSum(nums, target, expected):
    sol = Solution()
    result = sol.twoSum(nums, target)
    assert result == expected
