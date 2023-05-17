def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length_of_list = len(nums)
    for i in range(length_of_list-1):
        for j in range(i+1, length_of_list):
            if nums[i] + nums[j] == target:
                return [i, j]
