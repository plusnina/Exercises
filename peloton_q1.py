def func1(nums):
    max_diff = -1
    for i in range(0, len(nums)):
        max_var = nums[i]
        min_var = min(nums)
        if max_var-min_var>max_diff and nums.index(max_var)<nums.index(min_var):
            max_diff = max_var-min_var
    return max_diff

##checked with some longer arrays (but the session we had ended, I am sending you only the actual function.
