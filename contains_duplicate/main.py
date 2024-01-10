from collections import OrderedDict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not list(OrderedDict.fromkeys(nums).keys()) == nums
