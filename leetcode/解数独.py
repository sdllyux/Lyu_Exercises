
class Solution:
    def solveSudoku(self, board):
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案 
                return True
            i, j = empty[iter]
            b = (i // 3)*3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()
        print (board)


s=Solution()
s.solveSudoku([
[".",".","5","3",".",".",".",".","."],
["8",".",".",".",".",".",".","2","."],
[".","7",".",".","1",".","5",".","."],
["4",".",".",".",".","5","3",".","."],
[".","1",".",".","7",".",".",".","6"],
[".",".","3","2",".",".",".","8","."],
[".","6",".","5",".",".",".",".","9"],
[".",".","4",".",".",".",".","3","."],
[".",".",".",".",".","9","7",".","."]])


