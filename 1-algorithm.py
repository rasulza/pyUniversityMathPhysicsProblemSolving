"""

Complexity
    time    space

*first question*
example:
[5,4,2,6,234,2,23] ---> index 234 ---> 4
"""
nums = [5,4,2,6,234,2,23]

def show(list, element):
    for i in list:
        if i == element:
            return list.index(i)
        

print(show(nums, int(input("enter element"))))
    