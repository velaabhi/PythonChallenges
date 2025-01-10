'''

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.

Input Format - The first line of input contains the original string. The next line contains the substring.

Each character in the string is an ascii character.

Output Format - Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output  -  2
'''


'''
#1. Approach using find() of string
def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        # Find the next occurrence of the substring
        start = string.find(substring, start)
        print("start index - ",start)
        if start == -1:  # No more occurrences
            break
        count += 1
        start += 1  # Move start index to avoid overlapping matches
    return count

string = input("Enter String")
substring = input("Enter Sub String")
result = count_substring(string, substring)
print(result)
'''

'''
#2. Approach using findall() of regex

import re


string = "ABCDCDC"
substring = "CDC"
result = len(re.findall(f"(?={substring})", string))
print(result)  
'''


#3 Approach without inbuilt methods
string = "ABCDCDC"
substring = "CDC"

count = 0
n = len(substring)

for i in range(len(string) - n + 1):  # we have to only iterate for a part of index and not all the indices
    if string[i:i+n] == substring:
        count += 1

print(count)



