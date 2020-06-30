"""
input: J = "aA" S = "aAAbbbb"
output: 3
"""
J = input("J: ")
S = input("S: ")

print(sum(x in J for x in S))
