from test import test
from typing import List

class Robot:
    def __init__(self, index: int, pos: int, health: int, direction: str):
        self.robot_id: int = index
        self.position = pos
        self.health = health
        self.direction = direction

    def change_hp(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.health = 0

    def __gt__(self, other) -> bool:
        return True if self.health > other.health else False
    
    def __lt__(self, other) -> bool:
        return True if self.health < other.health else False
    
    def __eq__(self, other) -> bool:
        return True if self.health == other.health else False

def fight(robot_1: Robot, robot_2: Robot) -> tuple[Robot, int] | None:
    """
    Returns (Winner: Robot, loser_id: int)
    if robots have equal HP, returns None
    """
    if robot_1 > robot_2:
        robot_1.change_hp()
        return robot_1, robot_2.robot_id
    elif robot_1 < robot_2:
        robot_2.change_hp()
        return robot_2, robot_1.robot_id
    else:
        return None

class Solution:
    def survivedRobotsHealths(
        self,
        positions: List[int],
        healths: List[int],
        directions: str
    ) -> List[int]:
        
        if len(set(directions)) == 1:
            return healths

        alive: dict[int, Robot] = {
            robot_id: Robot(
                robot_id,
                positions[robot_id],
                healths[robot_id],
                directions[robot_id]
            ) for robot_id in range(len(positions))
        }
        robots_order: list[Robot] = list(
            sorted(alive.values(), key=lambda robot: robot.position)
        )

        lifo_right: list[Robot] = []

        index: int = 0

        while index < len(robots_order):
            robot: Robot = robots_order[index]
            if robot.direction == "R":
                lifo_right.append(robot)
            else:
                if lifo_right:
                    robot_2 = lifo_right.pop()
                    result = fight(robot, robot_2)
                    if result is None:
                        del alive[robot.robot_id]
                        del alive[robot_2.robot_id]
                    else:
                        winner, loser_id = result
                        del alive[loser_id]
                        if winner.direction == "R":
                            lifo_right.append(winner)
                        else:
                            if lifo_right:
                                continue
            index +=1
        result = [alive[i].health for i in sorted(alive.keys())]
        return result


if __name__ == "__main__":
    test_cases = {
        "TEST 1": {
            "args": ([5,4,3,2,1], [2,17,9,15,10], "RRRRR"),
            "kwargs": {},
            "answer": [2, 17, 9, 15, 10]
        },
        "TEST 2": {
            "args": ([3,5,2,6], [10,10,15,12], "RLRL"),
            "kwargs": {},
            "answer": [14]
        },
        "TEST 3": {
            "args": ([1,2,5,6], [10,10,11,11], "RLRL"),
            "kwargs": {},
            "answer": []
        },
        "TEST 4": {
            'args': ([1,40], [10,11], "RL"),
            "kwargs": {},
            "answer": [10]
        },
        "TEST 5": {
            'args': ([3,47], [46,26], "LR"),
            "kwargs": {},
            "answer": [46,26]
        }
    }
    test(Solution().survivedRobotsHealths, test_cases)