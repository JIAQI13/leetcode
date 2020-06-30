"""
input nums=[8,1,2,2,3]
output [4,0,1,1,3]
"""
input_string = input("input list with space: ")
input_list = input_string.split()
nums = []
for element in input_list:
    try:
        nums.append(int(element))
    except:
        print("wrong input")
        exit()
nums_old = list(nums) #or nums_old = nums * 1 #different ways of copying a list, if i do nums_old = nums it will just copy a pointer, which will be affected by nums.sort() 
nums.sort()
result = []
for element in nums_old:
    result.append(nums.index(element))
print(result)
