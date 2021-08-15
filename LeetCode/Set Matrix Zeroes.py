# Problem: https://leetcode.com/problems/set-matrix-zeroes/

from copy import deepcopy
from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        x_zero_coords = []
        y_zero_coords = []

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    x_zero_coords.append(y)
                    y_zero_coords.append(x)

        for y in x_zero_coords:
            matrix[y] = [0] * len(matrix[y])

        for x in y_zero_coords:
            for i in range(len(matrix)):
                matrix[i][x] = 0
