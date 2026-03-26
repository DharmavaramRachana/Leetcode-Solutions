class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # ---------- Helper: can we remove value d from a rectangle section? ----------
        def can_remove_from_horizontal_top(r: int, d: int, top_count: Counter) -> bool:
            height, width = r + 1, n
            area = height * width
            if area <= 1:
                return False

            if height > 1 and width > 1:
                return top_count[d] > 0
            if height == 1:  # single row
                return grid[0][0] == d or grid[0][n - 1] == d
            # width == 1: single column
            return grid[0][0] == d or grid[r][0] == d

        def can_remove_from_horizontal_bottom(r: int, d: int, bottom_count: Counter) -> bool:
            start = r + 1
            height, width = m - start, n
            area = height * width
            if area <= 1:
                return False

            if height > 1 and width > 1:
                return bottom_count[d] > 0
            if height == 1:  # single row
                return grid[start][0] == d or grid[start][n - 1] == d
            # width == 1: single column
            return grid[start][0] == d or grid[m - 1][0] == d

        def can_remove_from_vertical_left(c: int, d: int, left_count: Counter) -> bool:
            height, width = m, c + 1
            area = height * width
            if area <= 1:
                return False

            if height > 1 and width > 1:
                return left_count[d] > 0
            if width == 1:  # single column
                return grid[0][0] == d or grid[m - 1][0] == d
            # height == 1: single row
            return grid[0][0] == d or grid[0][c] == d

        def can_remove_from_vertical_right(c: int, d: int, right_count: Counter) -> bool:
            start = c + 1
            height, width = m, n - start
            area = height * width
            if area <= 1:
                return False

            if height > 1 and width > 1:
                return right_count[d] > 0
            if width == 1:  # single column
                return grid[0][start] == d or grid[m - 1][start] == d
            # height == 1: single row
            return grid[0][start] == d or grid[0][n - 1] == d

        # ---------- Try all horizontal cuts ----------
        top_sum = 0
        top_count = Counter()
        bottom_count = Counter()

        for i in range(m):
            bottom_count.update(grid[i])

        for r in range(m - 1):  # cut after row r
            row_sum = sum(grid[r])
            top_sum += row_sum
            for val in grid[r]:
                top_count[val] += 1
                bottom_count[val] -= 1
                if bottom_count[val] == 0:
                    del bottom_count[val]

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            d = abs(top_sum - bottom_sum)
            if top_sum > bottom_sum:
                if can_remove_from_horizontal_top(r, d, top_count):
                    return True
            else:
                if can_remove_from_horizontal_bottom(r, d, bottom_count):
                    return True

        # ---------- Try all vertical cuts ----------
        left_sum = 0
        left_count = Counter()
        right_count = Counter()

        for i in range(m):
            for j in range(n):
                right_count[grid[i][j]] += 1

        col_sums = [0] * n
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]

        for c in range(n - 1):  # cut after column c
            left_sum += col_sums[c]
            for i in range(m):
                val = grid[i][c]
                left_count[val] += 1
                right_count[val] -= 1
                if right_count[val] == 0:
                    del right_count[val]

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            d = abs(left_sum - right_sum)
            if left_sum > right_sum:
                if can_remove_from_vertical_left(c, d, left_count):
                    return True
            else:
                if can_remove_from_vertical_right(c, d, right_count):
                    return True

        return False