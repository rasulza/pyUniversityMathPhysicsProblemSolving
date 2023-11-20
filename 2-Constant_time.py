"""
Constant Time O(1)
"""

nums = [4, 4, 5, 6, 23, 645]

def show(list):
    if list[0] % 2 == 0:
        return "Even"
    return "odd"


print(show(nums))


