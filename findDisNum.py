def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # n = len(nums)
    # disappear = []
    # for i in range(1,n+1):
    #     if i not in nums:
    #         disappear.append(i)
    # return disappear
    for i in range(len(nums)):
        n = abs(nums[i])
        nums[n - 1] = -abs(nums[n - 1])
    ans = []
    for i in range(len(nums)):
        if nums[i] > 0:
            ans.append(i + 1)
    return ans
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))