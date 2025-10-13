"""
-create a function that sorts items in a list and stores them in a dictionary. 
- key is the index, values remain the same.
[2, 3, 5, 8, 1, 4]
- sort
- store in dict {key: value}
return dict
- push to github in a new branch - dict_values
- create a pull request
"""

def type_conversion(arr):
    arr.sort()
    new_dict = {}
    for ind, val in enumerate(arr):
        new_dict[ind] = val
    print(new_dict)


num = [2, 3, 5, 8, 1, 4]
type_conversion(num)