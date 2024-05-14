#NO NEED TO EXPORT MODULES, ONLY NEED TO import THEM OR USE from TO IMPORT THEIR METHODS FROM WITHIN OTHER FILES

def find_max(list_of_nums):
    maximum = list_of_nums[0] #Variable should be called anything besides "max" because max is actually a built in method in Python
    for num in list_of_nums:
        if num > maximum:
            maximum = num
    return maximum