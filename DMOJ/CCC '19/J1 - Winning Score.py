#*********************************************************/
# Problem: CCC '19 J1 - Winning Score
# Description: https://dmoj.ca/problem/ccc19j1
# Language: Python
# Created by: Willie Pai
# Date: 08/3/2019
#*********************************************************/

score = [0, 0]
for x in range (2):
		score[x] += int(input())*3
		score[x] += int(input())*2
		score[x] += int(input())
if score[0] > score[1]:
	print ('A')
elif score[1] > score[0]:
	print ('B')
else:
	print ('T')
