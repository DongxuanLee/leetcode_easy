def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set()
    for i in nums:
        if i not in nums_set:
            nums_set.add(i)
        else:
            nums_set.remove(i)
    return nums_set.pop()
if __name__ == "__main__":
    nums = [3,4,3,6]
    print(singleNumber(nums))