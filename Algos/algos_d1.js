"""
Input: s = "III"
Output: 3

Input: s = "IV"
Output: 4

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.


#if len = 1 return value 
#els if length s-1 < length s  (-) return value
els if length s -1 >lengths (+) return value
"""

def romanToInt(s):
    romans = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }
    total = romans.get(s[0])
    if len(s) > 1:
        for i in range(1, len(s), 1):
            total = total + romans.get(s[i])
            if romans.get(s[len(s)-1]) > romans.get(s[len(s)-2]):
                total = total - 2*(romans.get(s[len(s)-2]))
    return total

print(romanToInt("XXVI"))


    # for i in range(len(s)-1, 0, -1): 
    #     if romans.get(s[i]) > romans.get(s[i-1]):
    #         total = total + romans.get(s[i]) - romans.get(s[i-1])
    #     else:     
    #         total = total + romans.get(s[i])
    # return total


"""
start at end
check end val against next val
if end val is smaller, do subtraction
if end val is bigger, add
"""


