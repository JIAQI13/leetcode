"""
input nums=[1,2,3,4]
output [1,3,6,10]

constrain
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
input_string = input("Enter a list elements separated by space: ")
input_list = input_string.split()
nums = []
for i in input_list:
    try:
        nums.append(int(i))
    except:
        print("wrong input")
        exit()
result = []
sumnow = 0
for i in nums:
    sumnow = sumnow+i
    result.append(sumnow)
print(result)

