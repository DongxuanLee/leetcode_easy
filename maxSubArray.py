def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    list = []
    for i in nums:
        sum = i +sum
        if sum <0:
            sum = 0
        list.append(sum)
    print(max(list))
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(nums)