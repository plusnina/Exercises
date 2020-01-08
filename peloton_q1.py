def func1(nums):
    max_diff = -1
    for i in range(0, len(nums)-1):
        chk = nums[i]
        if chk-nums[i+1] >= max_diff:
            max_diff = chk-nums[i+1]
    return max_diff

##checked with some longer arrays (but the session we had ended, I am sending you only the actual function.