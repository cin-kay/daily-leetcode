# def sub_arr_sums(nums: list[int]):
#     arr_sums = []
#     w_size = len(nums)
#     i = 1
#     while i <= w_size:
#         curr_sum = sum(nums[:i])
#         arr_sums.append(curr_sum)
#         for j in range(i, len(nums)):
#             sub_sum = curr_sum - nums[j - i] + nums[j]
#             arr_sums.append(sub_sum)
#             curr_sum = sub_sum

#         i += 1


#     return arr_sums
def sub_arr_sums(nums: list[int]):
    arr_sums = []
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            arr_sums.append(sub_sum)

    return arr_sums


nums = [1, 2, 3, 4]
print(sub_arr_sums(nums))  # [1, 3, 6, 10, 2, 5, 9, 3, 7, 4]
