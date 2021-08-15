# Problem: https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Stores List[int] result
        result = []

        # Tracks which side of matrix to read from (0 = top, 1 = right, 2 = bottom, 3 = left)
        side_int = 0

        # Continuously reads each side of matrix until no more data is left to read
        while True:

            # If side to read is top
            if side_int == 0:

                # Extend entire top row of matrix to result and remove it from the matrix
                result.extend(matrix.pop(0))

            # If side to read is right
            elif side_int == 1:

                # Read each of the rows of the matrix from top to bottom
                for i in range(len(matrix)):
                    # Append the right-most element of the row to result, and remove it from the matrix
                    result.append(matrix[i].pop(len(matrix[i]) - 1))

                # If any rows become an empty list, remove it from the matrix
                for _ in range(matrix.count([])):
                    matrix.remove([])

            # If side to read is bottom
            elif side_int == 2:
                # Extend entire bottom row of matrix to result and remove it from the matrix
                result.extend(matrix.pop(len(matrix) - 1)[::-1])

            # If side to read is left
            elif side_int == 3:
                # Read each of the rows of the matrix from bottom to top
                for i in range(len(matrix) - 1, -1, -1):
                    # Append the leftmost element of the row to result, and remove it from the matrix
                    result.append(matrix[i].pop(0))

                # If any rows become an empty list, remove it from the matrix
                for _ in range(matrix.count([])):
                    matrix.remove([])

            # If there are no more elements left inside the matrix ([]), then stop
            if not matrix:
                break

            # Advance to next side to read from
            side_int = (side_int + 1) % 4

        return result
