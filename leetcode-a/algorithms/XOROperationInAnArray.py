"""
input n=5,start=0
output:8
nums[i]=start+2*i(0-indexed) and n == nums.length
"""
try:
    n = int(input("n: "))
    start = int(input("start: "))
except:
    print("wrong input")
    exit()

nums = []
for i in range(0,n):
    nums.append(start+2*i)
print(nums)
    
output = 0 #0^x=x x^x=0
for i in range(0,n):
    output = output ^ nums[i]
print(output)
    
