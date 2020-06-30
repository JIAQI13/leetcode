"""
input: num = 14
output: 6
different approach with even and odd numbers
"""
num = int(input("pls input n: "))
step = 0
while num != 0:
    if num%2 == 0:
        step = step + 1
        num = num / 2
    else:
        step = step + 1
        num = num-1
print(step)
