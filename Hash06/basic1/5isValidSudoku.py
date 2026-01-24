# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
 

# 注意：

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用 '.' 表示。

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # 检查第i行
            row_set = set()
            # 检查第i列
            col_set = set()
            
            for j in range(9):
                # 检查行
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                
                # 检查列
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
        
        # 检查3x3宫格
        for box_i in range(0, 9, 3):  # 宫格的起始行：0, 3, 6
            for box_j in range(0, 9, 3):  # 宫格的起始列：0, 3, 6
                box_set = set()
                for i in range(3):  # 宫格内的行偏移
                    for j in range(3):  # 宫格内的列偏移
                        row = box_i + i
                        col = box_j + j
                        if board[row][col] != '.':
                            if board[row][col] in box_set:
                                return False
                            box_set.add(board[row][col])
        
        return True