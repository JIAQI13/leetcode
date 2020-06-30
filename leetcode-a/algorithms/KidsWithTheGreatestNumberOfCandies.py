"""
input: candies =[2,3,5,1,3] extracandies = 3
output: [true,true,false,true]

"""
input_string = input("pls input a list with space(ex: 1 2 3 4): ")
input_list = input_string.split()
candies = []
for i in input_list:
    try:
        candies.append(int(i))
    except:
        print("wrong input")
        exit()

input_number = int(input("pls input a number of extra candles: "))
result = []
for i in candies:
    if i+input_number<max(candies):
       result.append(False)
    else:
        result.append(True)
print(result)
    

