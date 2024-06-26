class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        FINISH = n*n - 1
        
        def coordinate(dest):
            rem = dest // n
            row = n - 1 - rem
            if rem % 2 == 0:
                col = dest % n 
            else:
                col = n - 1 - (dest % n) 

            return row, col

        queue = deque([0])
        dist = [-1] * (n*n)
        dist[0] = 0

        while queue:
            dest = queue.popleft()
            x, y = coordinate(dest)

            for new_dest in range(dest + 1, min(dest + 6, n*n-1) + 1):
                new_x, new_y = coordinate(new_dest)
                if board[new_x][new_y] != -1:
                    new_dest = board[new_x][new_y] - 1

                if  dist[new_dest] == -1:
                    dist[new_dest] = dist[dest] + 1
                    queue.append((new_dest))

        return dist[n*n - 1]