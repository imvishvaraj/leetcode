class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    zero_rows.append(x)
                    zero_cols.append(y)

        for x in range(len(matrix)):
            if x in zero_rows:
                for y in range(len(matrix[x])):
                    matrix[x][y] = 0
            else:
                for y in range(len(matrix[x])):
                    if y in zero_cols:
                        matrix[x][y] = 0
        