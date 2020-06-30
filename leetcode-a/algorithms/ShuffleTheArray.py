"""
1470 shuffle the array
nums = [2,5,1,3,4,7] n=3
2 3 5 4 1 7
"""
input_string = input("pls input list with space: ")
input_list = input_string.split()
nums=[]
for i in input_list:
    try:
        nums.append(int(i))
    except:
        print("wrong input")
        exit()
print(nums)

try:
    input_num = int(input("pls input a number"))
except:
    print("wrong input")
    exit()

result = []
count = 0
for i in range(0, input_num):
    result.append(nums[i])
    result.append(nums[i+input_num])
print(result)
