'''
Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

'''
# M1 - by using textwrap module
import textwrap


def wrap(string, max_width):
    res = textwrap.fill(string, width=max_width)

    return res


if __name__ == '__main__':
    string, max_width = input("Enter text - "), int(input("Enter width - "))
    result = wrap(string, max_width)
    print(result)
'''

# M2 - conventional way by using str, list and join

s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4

l1 = list(s)
print(l1)

for i in range(4, len(l1)+5,5):
    l1.insert(i,"\n")

print(l1)
new_str = ''.join(l1)
print(new_str)