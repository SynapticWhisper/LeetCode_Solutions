from test import test
from typing import List

class Solution:
    TOTAL_SUM = sum(range(1, 10))
    VALUES = set(range(1, 10))
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Три проверки
        # 1) На общую сумму цифр в квадрате
        # 2) На вхождение в матрицу всех цифр от 1 до 9
        # 3) На сумму всех горизонталей, вертикалей и диогоналей (должны быть равны 15)

        def check_total_sum(grid: List[List[int]]) -> bool:
            result = sum([sum(row) for row in grid])
            return True if result == self.TOTAL_SUM else False

        def check_nums(grid: List[List[int]]) -> bool:
            test_value = set()
            for row in grid:
                test_value.update(row)
            return test_value == self.VALUES
        
        def check_sums(grid: List[List[int]]) -> bool:
            # Проверяем сумму диогоналей
            if sum([grid[0][0], grid[1][1], grid[2][2]]) != 15:
                return False
            if sum([grid[0][2], grid[1][1], grid[2][0]]) != 15:
                return False
            
            # Проверяем сумму строк
            for row in grid:
                if sum(row) != 15:
                    return False
            
            # Проверяем сумму столбцов
            rotated_grid = list(zip(*grid))[::-1]
            for row in rotated_grid:
                if sum(row) != 15:
                    return False
            
            return True
        
        # Определем максимальные индесы
        max_col_index = len(grid[0]) - 1
        max_row_index = len(grid) - 1

        # Задаем стартовую позицию
        rStart = 0
        rStop = 2
        cStart = 0
        cStop = 2

        result = 0

        def move_window() -> bool:
            nonlocal rStart, rStop, cStart, cStop

            if cStop < max_col_index:
                    cStart += 1
                    cStop += 1
                    return True
            else:
                if rStop < max_row_index:
                    rStart += 1
                    rStop += 1
                    cStart = 0
                    cStop = 2
                    return True
                else:
                    return False
            return False
        
        while cStop <= max_col_index and rStop <= max_row_index:
            grid_to_check = [
                grid[row][cStart:cStop+1] for row in range(rStart, rStop + 1)
            ]
            if not check_total_sum(grid_to_check):
                if move_window():
                    continue
                else:
                    break
            
            if not check_nums(grid_to_check):
                if move_window():
                    continue
                else:
                    break
            
            if not check_sums(grid_to_check):
                if move_window():
                    continue
                else:
                    break
            
            result += 1
            if move_window():
                continue
            else:
                break

        return result

test_cases = {
    "Test 1": {
        "args": (),
        "kwargs": {"grid": [[4,3,8,4],[9,5,1,9],[2,7,6,2]]},
        "answer": 1
    },
    "Test 2": {
        "args": (),
        "kwargs": {"grid": [[8]]},
        "answer": 0
    }
}


if __name__ == "__main__":
    test(Solution().numMagicSquaresInside, test_cases)