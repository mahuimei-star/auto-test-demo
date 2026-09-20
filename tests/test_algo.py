#这是取第二大数字的函数
def second_max(nums):
    new_nums = list(set(nums))
    if len(new_nums) < 2:
        return None
    else:
        new_nums.remove(max(new_nums))
    return max(new_nums)

#这是一个去重且按照原有顺序排布的函数
def dedup(nums):
    res=[]
    for i  in nums:
        if i not in res:
            res.append(i)
    return res
#这是一个对字符计数的函数
def count_chars(chars):
    res = {}
    for i in chars:
        res[i] = res.get(i, 0) + 1
    return res
import pytest
@pytest.mark.parametrize("nums, expect", [
    ([3, 1, 4, 4, 2], 3),
    ([5, 5, 5], None),
    ([7], None),
    ([], None),
])
def test_second_max(nums, expect):
    assert second_max(nums) == expect




