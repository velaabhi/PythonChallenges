'''
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, .
The next line contains an integer , the index location and a string , separated by a space.

Sample Input
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

Sample Output  -  abrackdabra
'''

def replace_char():
    s = 'abracadabra'
    #s = input("Enter String - ")

    position = 5
    #position = int(input("Enter the Pos "))

    character = 'k'
    #character = input("Enter the char you want to get as replacement")

    l1 = list(s)
    print("List is ",l1)
    l1[position] = character


    s2 = ''.join(l1)

    print(s)
    print(s2)

replace_char()