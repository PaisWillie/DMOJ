#*********************************************************/
# Problem: CCC '19 J3 - Cold Compress
# Description: https://dmoj.ca/problem/ccc19j3
# Language: Python
# Created by: Willie Pai
# Date: 08/3/2019
#*********************************************************/

def compression (text):
	lineOutput = ""
	char = text[0]
	count = 0
	for x in range (len(text)):
		if text[x] == char:
			count += 1
		else:
			lineOutput += str(count) + " " + char + " "
			char = text[x]
			count = 1
		if x == len(text) - 1:
			lineOutput += str(count) + " " + char + " "
	return lineOutput
lines = []
for _ in range (int(input())):
	lines.append(input())
for x in range (len(lines)):
	print (compression(lines[x]))
