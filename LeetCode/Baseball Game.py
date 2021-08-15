# Problem: https://leetcode.com/problems/baseball-game/

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for i in ops:
            if i == 'C':
                scores.pop()
            elif i == 'D':
                scores.append(scores[-1] * 2)
            elif i == '+':
                scores.append((scores[-1] + scores[-2]))
            else:
                scores.append(int(i))
        return sum(scores)
