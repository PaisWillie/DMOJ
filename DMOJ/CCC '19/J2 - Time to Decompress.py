#*********************************************************/
# Problem: CCC '19 J2 - Time to Decompress
# Description: https://dmoj.ca/problem/ccc19j2
# Language: Python
# Created by: Willie Pai
# Date: 08/3/2019
#*********************************************************/

def repeatPrint (num, char):
	output = ""
	for _ in range (int(num)):
		output += char
	return output
for x in range (int(input())):
	code = input().split(" ")
	print (repeatPrint(code[0], code[1]))
